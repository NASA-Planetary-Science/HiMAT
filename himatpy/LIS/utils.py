#!/usr/bin/env python
import os
import sys

import numpy as np
import xarray as xr

__author__ = ['Anthony Arendt', 'Landung Setiawan']


def get_xr_dataset(datadir, fname=None, multiple_nc=False):
    """
    Returns a "cleaned" xarray dataset for LIS data

    :param datadir: path to data ex. '/Users/lsetiawan/Downloads/200101/' or r'C:\work\datadrive\LIS\'
    :param fname: file name if using to open only one netCDF file
    :param multiple_nc: True if using to read multiple netCDF Files
    :return: xarray dataset
    """
    if multiple_nc is False:
        try:
            ds = xr.open_dataset(os.path.join(datadir, fname))
        except:
            print("Please provide filename!")
            sys.exit("Exiting...")
    else:
        ds = xr.open_mfdataset(os.path.join(datadir, '*.nc'))

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