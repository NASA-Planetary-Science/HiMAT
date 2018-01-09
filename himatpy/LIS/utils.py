#!/usr/bin/env python
import os
import sys
import glob
import re
import datetime

import pandas as pd
import numpy as np
import xarray as xr
from collections import OrderedDict
from dask.diagnostics import ProgressBar

__author__ = ['Anthony Arendt', 'Landung Setiawan']


def get_xr_dataset(datadir=None, fname=None, multiple_nc=False, files=[], **kwargs):
    """
    Reads in output from the NASA Land Information System (LIS) model.
    Returns a "cleaned" xarray dataset. Users can read a single or multiple NetCDF file(s). 

    :param datadir: path to directory containing the data, e.g. '/Users/lsetiawan/Downloads/200101/' or r'C:\work\datadrive\LIS\'
    :param fname: file name if only opening one NetCDF file
    :param multiple_nc: True if using to read multiple NetCDF Files
     **kwargs
        Arbitrary keyword arguments related to xarray open_dataset or open_mfdataset.
    :return: xarray dataset
    """
    if not multiple_nc:
        try:
            ds = xr.open_dataset(os.path.join(datadir, fname), **kwargs)
        except:
            print("Please provide filename!")
            sys.exit("Exiting...")
    else:
        if datadir:
            ds = xr.open_mfdataset(os.path.join(datadir, '*.nc'), **kwargs)
        elif files:
            ds = xr.open_mfdataset(files, **kwargs)
        else:
            print('Need either datadir or files for opening multiple netCDF')

    # some reformatting is necessary since LIS output does not follow CF conventions
    xmn = ds.attrs['SOUTH_WEST_CORNER_LON']
    ymn = ds.attrs['SOUTH_WEST_CORNER_LAT']
    dx = ds.attrs['DX']
    dy = ds.attrs['DY']
    nx = ds.dims['east_west']
    ny = ds.dims['north_south']
    x = np.arange(xmn, xmn + dx * nx, dx)
    y = np.arange(ymn, ymn + dy * ny, dy)
    # create tile from x, y
    data = np.tile(x, (ny, 1))
    ds.coords['longitude'] = (('north_south', 'east_west'), data)
    data = np.tile(y, (nx, 1))
    ds.coords['latitude'] = (('north_south', 'east_west'), np.swapaxes(data, 0, 1))

    return ds


def get_monthly_avg(ds, des_vars, export_nc=False, out_pth=None):
    ds_list = []
    for idx, var in enumerate(des_vars):
        with ProgressBar():
            da = ds[var].resample('MS', 'time', how = 'sum')
            new_ds.append(da)
    new_ds = xr.merge(ds_list)
    if export_nc:
        try:
            new_ds.to_netcdf(os.path.join(out_pth, 'LISMonthly.nc'))
        except IOError:
            print('Folder not found.')

    return new_ds


def process_da(da):
    """
    Assigns attributes and carries out unit conversions for variables selected from the LIS data.
    TODO: generalize for other variables / units. 

    Parameters
    ----------
    da : xarray data array
    Returns
    -------
    multda : xarray data array, with attributes and units modified
    """ 

    text = 'Daily {variable} in units of mm we'.format

    # attributes for the TWS:
    
    new_attrs = OrderedDict()
    for k, v in da.attrs.items():
        new_attrs.update({k:v})
    new_attrs.update({'units': 'mm we'})
    
    if da.attrs['standard_name'] == 'terrestrial_water_storage':
        new_attrs.update({'long_name': 'Daily change in water storage'})
        multda = da
    else:
        new_attrs.update({'long_name': text(variable=da.attrs['standard_name'])})
        multda = da * 86400
    
    multda.attrs = new_attrs
    
    return multda


def _filter_ncdf(ncdf, startyear=None, endyear=None):
    if startyear:
        ncdf = ncdf[(ncdf['time'] >= datetime.datetime(startyear, 1, 1))]
    if endyear:
        ncdf = ncdf[(ncdf['time'] <= datetime.datetime(endyear, 12, 31))]
    
    if startyear and endyear:
        ncdf = ncdf[(ncdf['time'] >= datetime.datetime(startyear, 1, 1)) & 
                    (ncdf['time'] <= datetime.datetime(endyear, 12, 31))]
        
    return ncdf


def process_lis_data(data_dir, ncpath, startyear=None, endyear=None, **kwargs):
    """
    This function reads daily LIS output, selects a subset of variables, and serializes to NetCDF files 
    with daily resolution and yearly span.
    
    Parameters
    ----------
    data_dir : String.
        The location of the Raw LIS NetCDF data
    nc_path : String.
        The location of the output NetCDF.
    startyear: Integer.
        The year to start processing.
    endyear: Integer.
        The year to end processing.
    **kwargs: Other keyword arguments associated with get_xr_dataset
    
    Returns
    -------
    None
    """
    
    # Get years
    all_nc = glob.glob(os.path.join(data_dir, '*.nc'))
    ncdf = pd.DataFrame({
        'files': all_nc,
    })
    
    ncdf['time'] = ncdf.apply(lambda x: pd.to_datetime(re.search(r'(\d)+', x['files']).group(0)), axis=1)
    ncdf = _filter_ncdf(ncdf, startyear, endyear)
        
    dt = pd.DatetimeIndex(ncdf['time'].values)
    year_starts = dt[dt.is_year_start].sort_values()
    year_ends = dt[dt.is_year_end].sort_values()
    yearslices = [(x,y) for x,y in zip(year_starts, year_ends)]
    print(yearslices)
        
    if not os.path.exists(ncpath):
        os.mkdir(ncpath)
    
    for ys, ye in yearslices:
        print('Processing {}...'.format(ys.year))
        yearfiles = ncdf[(ncdf['time'] > ys) & (ncdf['time'] < ye)]['files'].values
        # Open all files into a single xarray dataset
        ds = get_xr_dataset(files=sorted(yearfiles), multiple_nc=True, chunks={'time': 1})
        print('Subsetting data...')
        slicedds = ds[['Qsm_tavg','Rainf_tavg','Qs_tavg','Snowf_tavg','Qsb_tavg','Evap_tavg','TWS_tavg']]
        procds = slicedds.apply(lambda x: process_da(x))
        outname = os.path.join(ncpath, 'LIS_{}.nc'.format(ys.year))
        print('Exporting {}'.format(outname))
        with ProgressBar():
            procds.to_netcdf(outname)
        print('Clearing out memory...')
        slicedds = None
        procds = None
