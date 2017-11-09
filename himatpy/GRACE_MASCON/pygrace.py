# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division


# Import libraries to work with the data
import os
import sys

from branca.colormap import linear
import folium

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
    solution = f['solution']
    cmwe = solution['cmwe']
    time = f['time']

    avg_mass = []
    for idx, mascon in mascon_gdf.iterrows():
        avg_mass.append(perform_trend_analysis_cmwe(idx, cmwe, time))

    mascon_gdf['avg_mass_change_cm'] = avg_mass

    return mascon_gdf


# ------------ UTILITY FUNCTIONS ------------------------
# Function to create polygon from bounding coordinates
def polygeom(mascon_s):
    """
    Get polygon of a mascon.

    Parameters
    ----------
    mascon_s : Pandas Series.
        Mascon Series containing lat_center, lon_center, lat_span, and lon_span.
    Returns
    -------
    Shapely Polygon
        Polygon contructed from mascon bounding coordinates.
    """
    #     minx = (((mascon_s['lon_center'] - (mascon_s['lon_span'] / 2)) + 180) % 360) - 180
    #     maxx = (((mascon_s['lon_center'] + (mascon_s['lon_span'] / 2)) + 180) % 360) - 180
    minx = mascon_s['lon_center'] - (mascon_s['lon_span'] / 2)
    maxx = mascon_s['lon_center'] + (mascon_s['lon_span'] / 2)
    miny = mascon_s['lat_center'] - (mascon_s['lat_span'] / 2)
    maxy = mascon_s['lat_center'] + (mascon_s['lat_span'] / 2)
    return box(minx, miny, maxx, maxy)


def perform_trend_analysis_cmwe(mascon_idx, cmwe, time):
    mass = cmwe[mascon_idx, :]
    timeds = time['yyyy_doy_yrplot_middle']
    year = timeds[2, :]
    # Trend Analysis Equation
    fitfunc = lambda p, x: p[0] + p[1]*x + p[2]*np.cos(2.0*np.pi*x) + p[3]*np.sin(2.0*np.pi*x) + \
                    p[4]*np.cos(4.0*np.pi*x) + p[5]*np.sin(4.0*np.pi*x) + p[6]*np.cos(2.267*np.pi*x) + \
                    p[7]*np.sin(2.267*np.pi*x)
    errfunc = lambda p, x, y: fitfunc(p,x) - y
    # initial guess
    p0 = np.array([0.0, -5.0, 0.0, 0.0, 0.0, 0.0,0.0,0.0])
    # solved guess
    p1, success = scipy.optimize.leastsq(errfunc, p0[:], args=(year,mass))
    return p1[1]
