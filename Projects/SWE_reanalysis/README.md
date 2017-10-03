# HiMAT SWE Reanalysis - posterior SWE, SCA and forcing fields, Version 0

The HiMAT SWE Reanalysis fields, Version 0 is a data set of the posterior fields from the SWE reanalysis implementation (see Margulis et al., 2015; Cortés et al., 2016). Static and dynamic data is obtained from different sources including MERRA2, ASTER, SRTM, Landsat and the Global Land Cover Facility. Processing is done at the UCLA Hoffman2 Cluster.

## Overview

| | |
|---:|:---- |
| Platform/Product | SWE_REANALYSIS / POSTERIOR FIELDS |
| Gridded Resolution | 0.48 km|
| Effective Resolution| 0.48 km |
| Temporal Coverage | Oct. 2007 - Sep. 2008 (will be updated)|
| Temporal Resolution | Daily |
| Data Format | NetCDF (.nc) |
| Version | 0 |

## Data Description

The SWE reanalysis posterior fields consists of posterior SWE, SCA and forcing data for 1 x 1 degree tiles over the HMA region. For information on the methods please refer to Margulis et al., 2015. The files contain ensemble median values for each grid cell at a resolution of 480m.

### NetCDF format

|Variable Name (VARS)| Field | Units | Description | Dimension | Data Type | NoData |
|---------: | :----------: | :---: | :---------------------------------------------: | :----------------- | :-----------: |:-----:|
| FORCING_POST | Latitude | [°] | Latitude of the grid cell| 225 x 1| double | N/A |
| FORCING_POST | Longitude | [°] | Longitude of the grid cell | 225 x 1 | double | N/A |
| FORCING_POST | Ta_Post | [K] | Posterior air temperature ensemble median| 225 x 225 x 366 | 16-bit integer| -9999 |
| FORCING_POST | Rs_Post | [W/m^2] |Posterior incoming shortwave radiation ensemble median| 225 x 225 x 366 | 16-bit integer| -9999 |
| FORCING_POST | Rl_Post | [W/m^2] |Posterior incoming longwave radiation ensemble median| 225 x 225 x 366 | 16-bit integer| -9999 |
| FORCING_POST | Ps_Post | [Pa] |Posterior air pressure ensemble median| 225 x 225 x 366| 16-bit integer| -9999 |
| FORCING_POST | PPT_Post | [mm/day] |Posterior daily precipitation ensemble median| 225 x 225 x 366 | 16-bit integer| -9999 |
| SWE_SCA_POST | Latitude| [°] | Latitude of the grid cell| 225 x 1 | double | N/A |
| SWE_SCA_POST | Longitude | [°] | Longitude of the grid cell| 225 x 1 | double | N/A |
| SWE_SCA_POST | SWE_Post | [m] | Posterior grid-cell averaged SWE stats| 225 x 225 x 5 x 366| Double| -9999 |
| SWE_SCA_POST | SCA_Post | [-] | Posterior grid-cell averaged SCA stats| 225 x 225 x 5 x 366 | Double| -9999 |
| ALBEDO_POST | Latitude | [°] | Latitude of the grid cell| 225 x 1 | Double | N/A |
| ALBEDO_POST | Longitude | [°] | Longitude of the grid cell| 225 x 1 | double | N/A |
| ALBEDO_POST | Albedo | [-] |Albedo fractional value| 225 x 225 x 366 | Double | -9999 |

#### File Naming

```[hemisphere]_[llat]_0[hemisphere]_[llon]_0_agg_[agg_factor]_[VARS]_[WY].nc```

hemisphere - N or S for llat coordinate, W or E for llon coordinate

llat - lower left corner latitude of the tile (1° x 1° tile)

llon - lower left corner longitude of the tile (1° x 1° tile)

agg_factor - aggregation factor from 30m resolution (agg_factor = 16 => 480m, 0.48 km resolution)

VARS - variables included in the file

WY - water year of the file (Oct 1st. of one year to Sep 30th of the following year) e.g. 2007_08

#### Projection

+proj=laea +lat_0=40 +lon_0=105 +x_0=0 +y_0=0 +datum=WGS84 +units=° +no_defs

#### Spatial Coverage

Latitude bounds :defined by llat, + 1

Longitude bounds: defined by llon, + 1

## Sample Data

* TBD

## Data Access

### NASA ADAPT
* Datasets are located in the following folder on NASA ADAPT:

```
/att/pubrepo/hma_data/products/SWE/SWE_reanalysis
```

## Usage constraints

* data are preliminary and subject to change
* data are not for distribution outside of HiMAT

## Contact

* Steve Margulis

## References

* Cortés, G., Girotto, M., & Margulis, S. (2016). Snow process estimation over the extratropical Andes using a data assimilation framework integrating MERRA data and Landsat imagery. Water Resources Research, 52(4), 2582-2600.

* Margulis, S. A., Girotto, M., Cortés, G., & Durand, M. (2015). A particle batch smoother approach to snow water equivalent estimation. Journal of Hydrometeorology, 16(4), 1752-1772.