HiMAT Daily Surface Freeze/Thaw and Snowmelt Status, Version 1
===================================================

The HiMAT Daily Surface Freeze/Thaw and Snowmelt Status (F/T/M), Version 1 is a data set of the bulk landscape frozen, thawed or snowmelt status derived from enhanced resolution Advanced Scatterometer (ASCAT METOP-A). Data is obtained from the NASA sponsored Scatterometer Climate Record Pathfinder at Brigham Young University courtesy of David G. Long

## Overview
| | |
|---:|:---- |
| Platform/Product | ASCAT L1B SZF |
| Gridded Resolution | 4.45 km |
| Effective Resolution| 12-15 km |
| Temporal Coverage | Jan.2001 - Aug. 2016 (will be updated)|
| Temporal Resolution | Daily |
| Data Format | HDF(.h5), GeoTiff(.tif) |
| Version | 1 (revision 4) |

## Data Description

The ASCAT F/T/M record was derived from C-Band (5.255 GHz, vertical polarization) normalized backscatter measurements from the Advanced Scatterometer (ASCAT), 3-day(AM) overpass, resolution enhanced using the SIR algorithm (Early and Long, 2001). The timings and duration of snowmelt and freeze/thaw status are determined from time-series singularities (TSS) as described in Steiner and Tedesco (2014).

### GeoTiff format

|Band Number| Field | Units | Description | Dimension | Data Type | NoData|
|---------: | :----------: | :---: | :---------------------------------------------: | :----------------- | :-----------: |:-----:|
| 1 | Thaw_status | days | Number of thawed days for non-permanent snow/ice| 800 cols, 500 rows | 16-bit integer| -9999 |
| 2 | Thaw_status | days | Number of snowmelt days for permanent snow/ice | 800 cols, 500 rows | 16-bit integer| -9999 |

#### File Naming
``` radcwt_[version]_[region]_[subregion]_[instrument]_[mode]_[startDate]_[endDate]```

verion - Product version and revision
region - ASCAT region grid (BYU-SCP)
subregion - ASCAT subregion
instrument - Satellite instrument
mode - Data collection mode (BYU-SCP)
startDate - Product start date (YYYYMMDD)
endDate - Product end date (YYYYMMDD)

#### Projection
+proj=laea +lat_0=40 +lon_0=105 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs

#### Affine GeoTransform (GDAL)
```
[ GT1, GT2, GT3, GT4, GT5, GT6]
[-3510000.0, 4450.0, 0.0, 525000.0, 0.0, -4450.0]
```

#### Spatial Coverage
Latitude bounds : N 19.125, N 44.683 (DDeg)
Longitude bounds: E 63.427, E 105.577 (DDeg)

## Sample Data

<a href="http://himat.org/wp-content/uploads/2017/03/radcwt_1r4_China-Japan_hma_ascat_mafa_20100525_20100525_cwt.png"><img src="http://himat.org/wp-content/uploads/2017/03/radcwt_1r4_China-Japan_hma_ascat_mafa_20100525_20100525_cwt.png" alt="" width="2016" height="1008" class="alignnone size-full wp-image-602" /></a>

## Data Access

### NASA ADAPT

* [details on pathway to access the data on ADAPT]

### geoserver

### cloud storage
* [possibly link to cloud storage Nick provided]

## Usage constraints

* data are preliminary and subject to change
* data are not for distribution outside of HiMAT
* [additional details on usage agreements]

## Contact

* <a href="mailto:nsteiner@ccny.cuny.edu?Subject=ASCAT%20data" target="_top">Nick Steiner</a>  

## References

* D.S. Early and D.G. Long, "Image Reconstruction and Enhanced Resolution Imaging from Irregular Samples," IEEE
Transactions on Geoscience and Remote Sensing, Vol. 39, No. 2, pp. 291-302, 2001.

* N. Steiner, Marco Tedesco, 2014, A Wavelet Melt Detection Algorithm Applied to Enhanced Resolution Scatterometer Data
over Antarctica (2000-2009), Columbia University Academic Commons, http://dx.doi.org/10.7916/D8GF0TD5.