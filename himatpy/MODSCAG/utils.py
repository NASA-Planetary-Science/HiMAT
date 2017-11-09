# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import os
import sys
import glob
import json
import datetime
import shutil
import logging
import math
import warnings

import progressbar
import numpy as np
import rasterio
import xarray as xr
import pyproj
import re

from rasterio import windows
import rasterio as rio
from rasterio.transform import Affine
from rasterio import crs
from rasterio.warp import calculate_default_transform, reproject, Resampling


logger = logging.getLogger(__name__)

from himatpy.tools.snow_download_by_tile import (daterange, fetch_doys, generate_filepaths, TYPES)


__author__ = ['Landung Setiawan', 'Anthony Arendt']

bar = progressbar.ProgressBar()


def merge_tool(sources, bounds=None, res=None, nodata=None, precision=7):
    """Copy valid pixels from input files to an output file.

    All files must have the same number of bands, data type, and
    coordinate reference system.

    Input files are merged in their listed order using the reverse
    painter's algorithm. If the output file exists, its values will be
    overwritten by input values.

    Geospatial bounds and resolution of a new output file in the
    units of the input file coordinate reference system may be provided
    and are otherwise taken from the first input file.

    Parameters
    ----------
    sources: list of source datasets
        Open rasterio RasterReader objects to be merged.
    bounds: tuple, optional
        Bounds of the output image (left, bottom, right, top).
        If not set, bounds are determined from bounds of input rasters.
    res: tuple, optional
        Output resolution in units of coordinate reference system. If not set,
        the resolution of the first raster is used. If a single value is passed,
        output pixels will be square.
    nodata: float, optional
        nodata value to use in output file. If not set, uses the nodata value
        in the first input raster.

    Returns
    -------
    tuple

        Two elements:

            dest: numpy ndarray
                Contents of all input rasters in single array.

            out_transform: affine.Affine()
                Information for mapping pixel coordinates in `dest` to another
                coordinate system
    """
    first = sources[0]
    first_res = first.res
    nodataval = first.nodatavals[0]
    dtype = first.dtypes[0]

    # Extent from option or extent of all inputs.
    if bounds:
        dst_w, dst_s, dst_e, dst_n = bounds
    else:
        # scan input files.
        xs = []
        ys = []
        for src in sources:
            left, bottom, right, top = src.bounds
            xs.extend([left, right])
            ys.extend([bottom, top])
        dst_w, dst_s, dst_e, dst_n = min(xs), min(ys), max(xs), max(ys)

    logger.debug("Output bounds: %r", (dst_w, dst_s, dst_e, dst_n))
    output_transform = Affine.translation(dst_w, dst_n)
    logger.debug("Output transform, before scaling: %r", output_transform)

    # Resolution/pixel size.
    if not res:
        res = first_res
    elif not np.iterable(res):
        res = (res, res)
    elif len(res) == 1:
        res = (res[0], res[0])
    output_transform *= Affine.scale(res[0], -res[1])
    logger.debug("Output transform, after scaling: %r", output_transform)

    # Compute output array shape. We guarantee it will cover the output
    # bounds completely.
    output_width = int(math.ceil((dst_e - dst_w) / res[0]))
    output_height = int(math.ceil((dst_n - dst_s) / res[1]))

    # Adjust bounds to fit.
    dst_e, dst_s = output_transform * (output_width, output_height)
    logger.debug("Output width: %d, height: %d", output_width, output_height)
    logger.debug("Adjusted bounds: %r", (dst_w, dst_s, dst_e, dst_n))

    # create destination array
    dest = (np.ones((first.count, output_height, output_width), dtype=dtype) * 255.0).astype(dtype=dtype)

    if nodata is not None:
        nodataval = nodata
        logger.debug("Set nodataval: %r", nodataval)

    if nodataval is not None:
        # Only fill if the nodataval is within dtype's range.
        inrange = False
        if np.dtype(dtype).kind in ('i', 'u'):
            info = np.iinfo(dtype)
            inrange = (info.min <= nodataval <= info.max)
        elif np.dtype(dtype).kind == 'f':
            info = np.finfo(dtype)
            inrange = (info.min <= nodataval <= info.max)
        if inrange:
            dest.fill(nodataval)
        else:
            warnings.warn(
                "Input file's nodata value, %s, is beyond the valid "
                "range of its data type, %s. Consider overriding it "
                "using the --nodata option for better results." % (
                    nodataval, dtype))
    else:
        nodataval = 0

    for src in sources:
        # Real World (tm) use of boundless reads.
        # This approach uses the maximum amount of memory to solve the problem.
        # Making it more efficient is a TODO.

        # 1. Compute spatial intersection of destination and source.
        src_w, src_s, src_e, src_n = src.bounds

        int_w = src_w if src_w > dst_w else dst_w
        int_s = src_s if src_s > dst_s else dst_s
        int_e = src_e if src_e < dst_e else dst_e
        int_n = src_n if src_n < dst_n else dst_n

        # 2. Compute the source window.
        src_window = windows.from_bounds(
            int_w, int_s, int_e, int_n, src.transform,
            boundless=True, precision=precision)
        logger.debug("Src %s window: %r", src.name, src_window)

        # 3. Compute the destination window.
        dst_window = windows.from_bounds(
            int_w, int_s, int_e, int_n, output_transform,
            boundless=True, precision=precision)

        logger.debug("Dst window: %r", dst_window)

        # 4. Initialize temp array.
        tcount = first.count
        trows, tcols = tuple(b - a for a, b in dst_window)

        temp_shape = (tcount, trows, tcols)
        logger.debug("Temp shape: %r", temp_shape)

        temp = np.zeros(temp_shape, dtype=dtype)
        temp = src.read(out=temp, window=src_window, boundless=False,
                        masked=True)

        # 5. Copy elements of temp into dest.
        roff, coff = dst_window[0][0], dst_window[1][0]

        region = dest[:, roff:roff + trows, coff:coff + tcols]
        np.copyto(
            region, temp,
            where=np.logical_and(region == nodataval, temp.mask == False))

    return dest, output_transform


def create_tiles(hstart, hend, vstart, vend):
    '''
    Function to create list of tiles to download.
    In this case, MODIS tiles around lower 48 and central america are downloaded
    Tiles are based on sinusoidal projection by NASA
    '''

    h = []
    v = []
    tile = []

    for k in range(hstart, (hend + 2)):
        h.append(k)
    for l in range(vstart, (vend + 2)):
        v.append(l)
    for i in range(0, len(h) - 1):
        for j in range(0, len(v) - 1):
            if h[i] < 10 and v[i] >= 10:
                tile.append("h0" + str(h[i]) + "v" + str(v[j]))
            elif v[j] < 10 and h[i] >= 10:
                tile.append("h" + str(h[i]) + "v0" + str(v[j]))
            elif h[i] < 10 and v[j] < 10:
                tile.append("h0" + str(h[i]) + "v0" + str(v[j]))
            else:
                tile.append("h" + str(h[i]) + "v" + str(v[j]))
    return tile


def get_credentials(cred_json):
    with open(cred_json) as jsf:
        cred = json.load(jsf)

    return cred


def make_filepaths(start_date, end_date,
                   product_types, tiles, file_patterns):
    # Generate all the filepaths that will be downloaded by iterating over year, doy, and product types
    # Code snippet from snow_download_by_tile.py
    filepaths = []
    current_year = None
    available_doys = None
    for product_type in product_types:
        for year, doy in daterange(start_date, end_date):
            if current_year == year:
                pass
            else:
                current_year = year
                available_doys = fetch_doys(product_type, current_year)
            if doy in available_doys:
                filepaths += generate_filepaths(product_type, tiles, year, doy, file_patterns)
            else:
                bad_url = TYPES[product_type]['url'].format(year=year, doy=doy)
                print("Unable to download:: %s" % (bad_url,))

    return filepaths


def merge_tiles(alldirs, desired_dir, file_patterns, epsg=None, exportnc=False):
    out_name = 'MOD09GA_{varname}_{date}_HMA{epsg}.tif'.format
    print('Merging tiles ...')

    for d in bar(alldirs):
        gtiffs = glob.glob(os.path.join(os.path.abspath(d), file_patterns))
        date = datetime.datetime.strptime(d, 'modscag-historic/%Y/%j')

        with rio.Env():
            output = out_name(varname=file_patterns.replace('*', '').replace('.tif', ''),
                              date='{:%Y_%m_%d}'.format(date), epsg='')
            sources = [rio.open(f) for f in gtiffs]
            data, output_transform = merge_tool(sources, nodata=255)
            print(data.dtype)

            profile = sources[0].profile
            print(profile)
            # profile.pop('affine')
            profile['transform'] = output_transform
            profile['height'] = data.shape[1]
            profile['width'] = data.shape[2]
            profile['driver'] = 'GTiff'
            profile['nodata'] = 255
            print('Merged Profile:')
            print(profile)

            with rio.open(os.path.join(desired_dir, output), 'w', **profile) as dst:
                dst.write(data)

            if epsg:
                try:
                    varname = file_patterns.replace('*', '').replace('.tif', '')
                    reproj_out = out_name(varname=varname,
                                          date='{:%Y_%m_%d}'.format(date),
                                          epsg='_{}'.format(epsg))
                    print(output)
                    reproj_tiff(os.path.join(desired_dir, output),
                                os.path.join(desired_dir, reproj_out), epsg)
                    if exportnc:
                        print('Exporting to netCDF...')
                        if epsg == 4326:
                            rasterio_to_xarray(os.path.join(desired_dir, reproj_out), varname)
                        else:
                            print('Projection must be EPSG:4326!')
                            sys.exit()
                except:
                    print('Invalid EPSG Code. Go to http://epsg.io/')

        if os.path.exists(os.path.join(desired_dir, d)):
            shutil.rmtree(os.path.join(desired_dir, d))

        shutil.copytree(d, os.path.join(desired_dir, d))
    # Cleanup..
    shutil.rmtree(os.path.dirname(os.path.dirname(alldirs[0])))


def reproj_tiff(gtiff, output, epsg):
    dst_crs = crs.CRS.from_epsg(epsg)

    with rio.Env(CHECK_WITH_INVERT_PROJ=True):
        with rio.open(gtiff) as src:
            profile = src.profile

            # Calculate the ideal dimensions and transformation in the new crs
            dst_affine, dst_width, dst_height = calculate_default_transform(
                src.crs, dst_crs, src.width, src.height, *src.bounds)

            # update the relevant parts of the profile
            profile.update({
                'crs': dst_crs,
                'transform': dst_affine,
                'width': dst_width,
                'height': dst_height
            })
            print('Reprojected profile:')
            print(profile)

            with rio.open(output, 'w', **profile) as dst:
                reproject(
                    # Source parameters
                    source=rio.band(src, 1),
                    src_crs=src.crs,
                    src_transform=src.transform,
                    # Destination paramaters
                    destination=rio.band(dst, 1),
                    dst_transform=dst_affine,
                    dst_crs=dst_crs,
                    # Configuration
                    resampling=Resampling.nearest,
                    num_threads=2)


def rasterio_to_xarray(fname, varname):
    with rio.Env(CHECK_WITH_INVERT_PROJ=True):
        with rasterio.open(fname) as src:
            print(vars(src.profile))
            data = src.read()
            data = np.where(data == src.nodata, np.nan, data)
            data = np.where(data == 235, np.nan, data)
            # data = np.expand_dims(data[0], axis=0)

            # Get coords
            nx, ny = src.width, src.height
            x0, y0 = src.bounds.left, src.bounds.top
            dx, dy = src.res[0], -src.res[1]

            coords = {'time': [
                datetime.datetime.strptime(re.search(r'(\d+_\d+_\d+)', fname).group(1), '%Y_%m_%d')],
                      'lat': np.arange(start=y0, stop=(y0 + ny * dy), step=dy),
                      'lon': np.arange(start=x0, stop=(x0 + nx * dx), step=dx)}
            # Get dims
            dims = ('time', 'lat', 'lon')

            attrs = {}
            attrs['crs'] = src.crs.get('init').upper()
            for attr_name in ['transform', 'nodata']:
                try:
                    attrs[attr_name] = getattr(src, attr_name)
                except AttributeError:
                    pass
    dataset = xr.DataArray(data,
                           dims=dims,
                           name=varname,
                           coords=coords,
                           attrs=attrs).sortby('lat').to_dataset()

    dataset.to_netcdf(path=fname.replace('.tif', '.nc'),
                 format='NETCDF4',
                 encoding={
                     'snow_fraction': {'dtype': 'float64',
                                       'scale_factor': 0.1,
                                       '_FillValue': -9999,
                                       'zlib': True}
                 },
                 unlimited_dims='time')
