## Scripts to access MODIS Snow Covered-Area and Grain size (MODSCAG) datasets

This script helps HiMAT users acquire MODSCAG products specifically for the HMA region. It builds from a [Python script](https://github.com/NASA-Planetary-Science/HiMAT/blob/master/scripts/tools/snow_download_by_tile.py) provided by JPL.

### Data access

Users must first require a username and password from the JPL [snow data portal](https://snow.jpl.nasa.gov/portal/data/help_modscag). 

### Script Usage: 

```bash
modscag_download.py [-h] [--enddate ENDDATE] CRED VARS STARTDATE OUTPATH
```

positional arguments:

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

### Example: 

```bash
python modscag_download.py .cred.json snow_fraction 20000224 --enddate 20000308 /att/nobackup/aarendt/modscag/
```

### Output:

The script will download only those tiles that overlap with the HMA region already defined by the HiMAT team. It will output one geotiff per day that contains all the tiles mosaicked together. The output format is:

```bash
MOD09GA_VAR_YYYY_MM_DD_HMA.tif
```