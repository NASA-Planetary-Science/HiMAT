# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import os
import sys
import datetime
import argparse

import progressbar

from himatpy.MODSCAG.utils import (create_tiles, get_credentials, make_filepaths, merge_tiles,
                                   rasterio_to_xarray)
from himatpy.tools.snow_download_by_tile import (setup_auth, download_file, SNOW_DATA_URL)


bar = progressbar.ProgressBar()


def make_parser():
    parser = argparse.ArgumentParser(description='Process some integers. '
                                                 'Example: python modscag_download.py .cred.json '
                                                 'snow_fraction 20000224 --enddate 20000225 /Users/lsetiawan/Desktop/Himatstuff/')
    parser.add_argument('credential', metavar='CRED', type=str,
                        help='''Credential file name, full path is better. 
                        Should be json and follow this pattern: {"user": "username","password": "password"}''')
    parser.add_argument('varnames', metavar='VARS', type=str,
                        help='Variables desidered, comma separated if multiple')
    parser.add_argument('startdate', metavar='STARTDATE', type=str, help='Start Date yyyymmdd')
    parser.add_argument('--enddate', type=str, help='End Date yyyymmdd or if blank it will be today')
    parser.add_argument('--reproj', type=int, help='EPSG CODE to reproject merged tile to. You can find epsg code in http://epsg.io/')
    parser.add_argument('outpath', metavar='OUTPATH', type=str, help='File output path, this is where merged tiff and raw dataset will be stored')
    parser.add_argument('--exportnc', action="store_true", default=False, help='Optional to export to netCDF file, needs to reproject to EPSG:4326 to work!')


    return parser


if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()

    if not os.path.exists(args.outpath):
        os.makedirs(args.outpath)

    dtform = '{:%Y%j}'.format
    startdate = datetime.datetime.strptime(args.startdate, '%Y%m%d')
    enddate = datetime.datetime.today()
    if not args.startdate:
        print('Please provide a start date!')
        sys.exit()
    if args.enddate:
        enddate = datetime.datetime.strptime(args.enddate, '%Y%m%d')

    # HMA Region
    tiles = create_tiles(22, 28, 4, 6)
    varnames = args.varnames.split(',')
    patterns = ','.join(['*{}.tif'.format(v.strip(' ')) for v in varnames])

    cred = get_credentials(args.credential)

    options = {
        'user': cred['user'],
        'passwd': cred['password'],
        'product_types': 'MODSCAG'.split(','),
        'start': startdate,
        'end': enddate,
        'file_patterns': patterns,
        'tiles': tiles
    }

    # Setup login
    setup_auth(options['user'], options['passwd'])

    filepaths = make_filepaths(start_date=options['start'],
                               end_date=options['end'],
                               product_types=options['product_types'],
                               tiles=options['tiles'],
                               file_patterns=options['file_patterns'])

    dirlist = []
    for filepath in bar(filepaths):
        dirlist.append(os.path.dirname(filepath[len(SNOW_DATA_URL) + 1:]))
        download_file(filepath)

    alldirs = list(set(dirlist))

    merge_tiles(alldirs, args.outpath, options['file_patterns'], args.reproj, args.exportnc)