## Scripts to access MODIS Snow Covered-Area and Grain size (MODSCAG) datasets

This script helps HiMAT users acquire MODSCAG products specifically for the HMA region. It builds from a [Python script](https://github.com/NASA-Planetary-Science/HiMAT/blob/master/scripts/tools/snow_download_by_tile.py) provided by JPL.

Note: For reprojecting the output merged tiles, we used a nearest resampling method.

### Data access

Users must first require a username and password from the JPL [snow data portal](https://snow.jpl.nasa.gov/portal/data/help_modscag). 

### Script Usage: 

```bash
modscag_download.py [-h] [--enddate ENDDATE] [--reproj EPSGCODE] CRED VARS STARTDATE OUTPATH
```

Note that we have put `modscag_download.py` in the root directory of this GitHub repository.

### positional arguments:

| arguments | description |
|:----|:----|
| CRED | Credential file name, full path is better. Should be json and follow this pattern: {“user”: “username”,“password”:                “password”} |
| VARS | Variables desidered, comma separated if multiple |
| STARTDATE | Start Date yyyymmdd |
| OUTPATH |  File output path, this is where merged tiff and raw                    dataset will be stored |

optional arguments:

| arguments | description |
|:----|:----|
| -h, --help | show this help message and exit |
| --enddate ENDDATE | End Date yyyymmdd or if blank it will be today |
| --reproj EPSGCODE | EPSG CODE to reproject merged tile to. You can find epsg code in http://epsg.io/ |

### Example: 

```bash
python modscag_download.py .cred.json snow_fraction 20000224 --enddate 20000308 --reproj 4326 /att/nobackup/aarendt/modscag/
```

### Output:

The script will download only those tiles that overlap with the HMA region already defined by the HiMAT team. It will output one geotiff per day that contains all the tiles mosaicked together. The output format is:

```bash
MOD09GA_VAR_YYYY_MM_DD_HMA.tif
```

For reprojected tiles it would be:
```bash
MOD09GA_VAR_YYYY_MM_DD_HMA_EPSGCODE.tif
```

## Other tools

Visit David Shean's [GitHub page](https://github.com/dshean/snowtools) to access additional tools for retrieval and processing of MODSCAG products.
