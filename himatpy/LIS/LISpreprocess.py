#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from himatpy.LIS import utils as LISutils

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='LISpreprocess.py', epilog=None,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument('lisdir', metavar='<LISDIR>', type=str,
                        help="The directory of Raw LIS NetCDF")
    parser.add_argument('outdir', metavar='<OUTDIR>', type=str,
                        help="The directory for the preprocessed data")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    
    args = parser.parse_args()
    
    if args.lisdir and args.outdir:
        LISutils.process_lis_data(args.lisdir, args.outdir)
    else:
        print('ERROR..')
        sys.exit()
    
