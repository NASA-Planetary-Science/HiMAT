#!/usr/bin/env python
import os
import sys

import pandas as pd
import numpy as np
import xarray as xr
import progressbar
from collections import OrderedDict
from dask.diagnostics import ProgressBar

__author__ = ['Anthony Arendt', 'Landung Setiawan']


def get_xr_dataset(datadir, fname=None, multiple_nc=False, **kwargs):
    """
    Returns a "cleaned" xarray dataset for LIS data

    :param datadir: path to data ex. '/Users/lsetiawan/Downloads/200101/' or r'C:\work\datadrive\LIS\'
    :param fname: file name if using to open only one netCDF file
    :param multiple_nc: True if using to read multiple netCDF Files
     **kwargs
        Arbitrary keyword arguments related to xarray open_dataset or open_mfdataset.
    :return: xarray dataset
    """
    if multiple_nc is False:
        try:
            ds = xr.open_dataset(os.path.join(datadir, fname), **kwargs)
        except:
            print("Please provide filename!")
            sys.exit("Exiting...")
    else:
        ds = xr.open_mfdataset(os.path.join(datadir, '*.nc'), **kwargs)

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
    # attributes for the first 6 variables:
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


def process_lis_data(data_dir, ncpath, **kwargs):
    """
    This function process LIS Data by breaking it up into yearly netcdf. Only certain variables are exported.
    
    Parameters
    ----------
    data_dir : String.
        The location of the Raw LIS NetCDF Data
    nc_path : String.
        The location of the output NetCDF.
    **kwargs: Other keyword arguments that works with get_xr_dataset
    
    Returns
    -------
    None
    """
    # Open all files into a single xarray dataset
    print('Reading in all LIS data...')
    ds = get_xr_dataset(data_dir, fname=None, multiple_nc=True, chunks={'time': 1})
    print('Subsetting data...')
    desiredds = ds[['Qsm_tavg','Rainf_tavg','Qs_tavg','Snowf_tavg','Qsb_tavg','Evap_tavg','TWS_tavg']]
    
    dt = pd.DatetimeIndex(desiredds.coords['time'].values)
    year_starts = dt[dt.is_year_start]
    year_ends = dt[dt.is_year_end]
    yearslices = [(x,y) for x,y in zip(year_starts, year_ends)]
    
    if not os.path.exists(ncpath):
        os.mkdir(ncpath)
    
    bar = progressbar.ProgressBar()
    for ys, ye in bar(yearslices):
        print('Processing {}...'.format(ys.year))
        slicedds = desiredds.sel(time = slice(ys, ye))
        procds = slicedds.apply(lambda x: process_da(x))
        procds.to_netcdf(os.path.join(ncpath, 'LIS_{}.nc'.format(ys.year)))
        print('Clearing out memory...')
        slicedds = None
        procds = None
