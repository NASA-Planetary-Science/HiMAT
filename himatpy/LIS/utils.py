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


def get_xr_dataset(datadir=None, fname=None, multiple_nc=False, twoDcoords=False, files=[], keepVars=[], **kwargs):
    """
    Reads in output from the NASA Land Information System (LIS) model.
    Returns a "cleaned" xarray dataset. Users can read a single or multiple NetCDF file(s). 

    :param datadir: path to directory containing the data, e.g. '/Users/lsetiawan/Downloads/200101/' or r'C:\work\datadrive\LIS\'
    :param fname: file name if only opening one NetCDF file
    :param multiple_nc: True if using to read multiple NetCDF Files
    :param twoDcoords: True if you want multidimensional coordinates
    :param delVars: list of variables to be retained 
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

    # first, optional selection of user-specified variables. This has to occur before the coordinate
    # manipulations below
    
    if keepVars:
        try:
            products = [x for x in ds]
            deleted_vars = [y for y in products if y not in keepVars]
            ds = ds.drop(deleted_vars)
        except:
            print("List of variables to keep does not match variable names in the dataset.")
            sys.exit("Exiting...")
        
    xmn = ds.attrs['SOUTH_WEST_CORNER_LON']
    ymn = ds.attrs['SOUTH_WEST_CORNER_LAT']
    dx = ds.attrs['DX']
    dy = ds.attrs['DY']
    nx = ds.dims['east_west']
    ny = ds.dims['north_south']
    x = np.arange(xmn, xmn + dx * nx, dx)
    y = np.arange(ymn, ymn + dy * ny, dy)
    if twoDcoords:
        # create tile from x, y
        data = np.tile(x, (ny, 1))
        ds.coords['long'] = (('north_south', 'east_west'), data)
        data = np.tile(y, (nx, 1))
        ds.coords['lat'] = (('north_south', 'east_west'), np.swapaxes(data, 0, 1))
    else:     
        ds.coords['long'] = (('east_west'), x)
        ds.coords['lat'] = (('north_south'), y)

    # rename the dimensions to be lat/long so that other himatpy utilities are consistent with this
    ds.rename({'east_west':'long', 'north_south':'lat'}, inplace = True)

    return ds


def resample_da(da):
    """
    Resample data array and assigns attributes for variables selected from the LIS data.
    TODO: generalize for other variables / units. 

    Parameters
    ----------
    da : xarray data array
    Returns
    -------
    da_monthly : xarray data array, with attributes and units modified
    """ 
    da_monthly = da.resample('MS', 'time', how = 'sum')
    text = 'Cumulative monthly {variable} in units of mm we'.format
    
    new_attrs = OrderedDict()
    for k, v in da.attrs.items():
        new_attrs.update({k:v})
    new_attrs.update({'units': 'mm we'})
    
    if da.attrs['standard_name'] == 'terrestrial_water_storage':
        new_attrs.update({'long_name': 'Cumulative in monthly water storage'})
    else:
        new_attrs.update({'long_name': text(variable=da.attrs['standard_name'])})
    
    da_monthly.attrs = new_attrs
    
    return da_monthly


def get_monthly_avg(ds, export_nc=False, out_pth=None):
    monthlyds = ds.apply(lambda x: resample_da(x))
    
    if export_nc and out_pth:
        try:
            fname = os.path.join(out_pth, 'LISMonthly.nc')
            print('Exporting {}'.format(fname))
            with ProgressBar():
                monthlyds.to_netcdf(fname)
        except IOError:
            print('Folder not found.')

    return monthlyds


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
