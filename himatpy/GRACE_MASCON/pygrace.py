# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division


# Import libraries to work with the data
import os
import sys

import geopandas as gpd
from geopandas import GeoDataFrame

import h5py
import numpy as np
import pandas as pd
import pyepsg
import scipy.optimize
from shapely.geometry import (Point, box)


CRS = pyepsg.get(4326).as_proj4()

def extract_grace(fpath):
    """
    Creates a file object for extracting GRACE data from NASA GSFC mascon product.

    Parameters
    ----------
    fpath : string
       path to the GRACE hdf5 file
    Returns
    -------
    f : file object
        h5py file object
    """
    try:
        f = h5py.File(fpath)
    except:
        sys.exit('File Not Found.')

    groups = list(f.keys())
    print('Data extracted: ')
    for g in groups:
        group = f[g]
        print('---')
        print('Group: {}'.format(g))
        print('---')
        for d in group.keys():
            print(group[d])

    return f


def get_mascon_gdf(mascon_ds):
    """
    converts the mascon group in the hdf5 file to a geodataframe

    Parameters
    ----------
    mascon_ds : HDF5 group
       the HDF5 group labeled "mascon"
    
    Returns
    -------
    mascon_gdf : geodataframe
       a geodataframe with the same data as in the HDF5 group
    """
    mascon_dct = {}
    poly_geom = []

    dataset_list = list(mascon_ds.keys())
    for d in dataset_list:
        mascon_dct.update({
            d: mascon_ds[d][0, :]
        })

    mascon_df = pd.DataFrame.from_dict(mascon_dct)
    for k, m in mascon_df.iterrows():
        poly_geom.append(polygeom(m))

    mascon_gdf = GeoDataFrame(mascon_df, crs=CRS, geometry=poly_geom)

    print('There are {} Mascons in this dataset.'.format(len(mascon_gdf)))

    return mascon_gdf


def get_cmwe_trend_analysis(mascon_gdf, f):
    """
    calculates the linear trend in mass change at each mascon.

    Parameters
    ----------
    mascon_gdf : geodataframe.
        geodataframe containing the GRACE time series data
    f : h5py file object 
        points to the GRACE input file; instantiated in 'extract_grace' function above

    Returns
    -------
    mascon_gdf : geodataframe.
        modified with a new column containing the linear trend in mass    
    """
    solution = f['solution']
    cmwe = solution['cmwe']
    time = f['time']
    avg_mass = []

  # trend analysis returns the full parameter set. Parameter [1] is the linear slope
    for idx, mascon in mascon_gdf.iterrows():
        avg_mass.append(trend_analysis(time['yyyy_doy_yrplot_middle'][2, :], cmwe[mascon.mascon, :], optimization = True)[1])
  
    mascon_gdf['avg_mass_change_cm'] = avg_mass

    return mascon_gdf


# ------------ UTILITY FUNCTIONS ------------------------
# Function to create polygon from bounding coordinates
def polygeom(mascon_s):
    """
    Generates a polygon feature from GRACE mascon coordinates.

    Parameters
    ----------
    mascon_s : Pandas Series.
        Mascon Series containing lat_center, lon_center, lat_span, and lon_span.
    Returns
    -------
    Shapely Polygon
        Polygon contructed from mascon bounding coordinates.
    """
    minx = mascon_s['lon_center'] - (mascon_s['lon_span'] / 2)
    maxx = mascon_s['lon_center'] + (mascon_s['lon_span'] / 2)
    miny = mascon_s['lat_center'] - (mascon_s['lat_span'] / 2)
    maxy = mascon_s['lat_center'] + (mascon_s['lat_span'] / 2)
    return box(minx, miny, maxx, maxy)

def trend_analysis(dec_year, series=None, optimization=False, pvalues = None):
    """
    Fits a second order sinusoidal polynomial equation to a time series using least-squares optimization.

    Parameters
    ----------
    series : an array representing the data 
    dec_year: an array of decimal years
    optimization: TRUE if being used to generate a least squares fit
    
    Returns
    -------
    CASE optimization = TRUE
       fitted_coefficients: a list of the 7 coefficients derived from the least-squares fit
    CASE optimization = FALSE
       series_fit: a new series generated from the user-provided pvalues 
    """

    # Trend Analysis Equation
    fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*np.cos(2.0*np.pi*x) + p[3]*np.sin(2.0*np.pi*x) + \
                    p[4]*np.cos(4.0*np.pi*x) + p[5]*np.sin(4.0*np.pi*x) + p[6]*np.cos(2.267*np.pi*x) + \
                    p[7]*np.sin(2.267*np.pi*x)

    if optimization:
        errfunc = lambda p, x, y: fitfunc(p,x) - y
        # initial guess
        p0 = np.array([0.0, -5.0, 0.0, 0.0, 0.0, 0.0,0.0,0.0])
        # solved guess
        fitted_coefficients, success = scipy.optimize.leastsq(errfunc, p0[:], args=(dec_year,series))
        return fitted_coefficients
    try:
        series_fit = fitfunc(pvalues, dec_year)
        return series_fit
    except:
        print("no pvalues!") 
        

def build_mask(dsbbox, mascon_gdf, dacoords, serialize=False, datadir=None):
    """
    dsbbox: List or Tuple 
        minx, miny, maxx, maxy
    """
    # Build a polygon around the extent of the LIS output so we can subset the GRACE data
    coords = [(dsbbox[0],dsbbox[1]), (dsbbox[0],dsbbox[3]), (dsbbox[2],dsbbox[3]), (dsbbox[2], dsbbox[1])]
    # Create a Shapely polygon from the coordinate-tuple list
    lispoly = Polygon(coords)
    df = pd.DataFrame.from_records([{'region_name': 'dataset'}])
    geometry = [lispoly]
    regiondf = gpd.GeoDataFrame(df, geometry=geometry, crs={'init': 'epsg4326'})
    
    gpd_intersect = gpd.overlay(regiondf, mascon_gdf, how='intersection')
    
    # Create mask
    numbers = gpd_intersect.index.values
    names = gpd_intersect['mascon'].values
    abbrevs = gpd_intersect['mascon'].values
    m = regionmask.Regions_cls('region_mask',numbers,names,abbrevs,gpd_intersect.geometry.values)
    m.name = 'mascon'
    
    gracemsk = m.mask(dacoords, lon_name = 'longitude', lat_name = 'latitude')
    gracemsk.name = 'mask'
    
    if serialize:
        if datadir:
            gracemsk.to_netcdf(os.path.join(datadir, 'gracemsk.nc'))
        else:
            print('Need datadir to be specified.')
    return gracemsk
