# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import os
import glob
import json
import datetime
import shutil

import progressbar

import rasterio as rio
from rasterio.merge import merge as merge_tool

from scripts.tools.snow_download_by_tile import (daterange, fetch_doys,
                                                 generate_filepaths, TYPES)


__author__ = ['Landung Setiawan', 'Anthony Arendt']

bar = progressbar.ProgressBar()


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


def merge_tiles(alldirs, desired_dir, file_patterns):
    out_name = 'MOD09GA_{varname}_{date}_HMA.tif'.format
    print('Merging tiles ...')

    for d in bar(alldirs):
        gtiffs = glob.glob(os.path.join(os.path.abspath(d), file_patterns))
        date = datetime.datetime.strptime(d, 'modscag-historic/%Y/%j')

        with rio.Env():
            output = out_name(varname=file_patterns.replace('*', '').replace('.tif', ''),
                              date='{:%Y_%m_%d}'.format(date))
            sources = [rio.open(f) for f in gtiffs]
            data, output_transform = merge_tool(sources)

            profile = sources[0].profile
            profile.pop('affine')
            profile['transform'] = output_transform
            profile['height'] = data.shape[1]
            profile['width'] = data.shape[2]
            profile['driver'] = 'GTiff'
            profile['nodata'] = 255
            print(profile)

            with rio.open(os.path.join(desired_dir, output), 'w', **profile) as dst:
                dst.write(data)

        shutil.copytree(d, os.path.join(desired_dir, d))
        shutil.rmtree(os.path.dirname(os.path.dirname(d)))
