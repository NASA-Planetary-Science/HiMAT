NASA LIS Initial Results Over HMA
=================================

# Overview

This initial result is simulated from the NASA Land Information System ([LIS](http://lis.gsfc.nasa.gov); Kumar et al. 2006) with Noah-MP 3.6 over the High Mountain Asia (HMA). The NASA Modern Era Retrospective-Analysis for Research and Applications 2 (MERRA-2) is used as meteorological forcings. To improve the spatial representativeness of the precipitation fields and to include orographic signature for modeling at 1 km resolution, the input fields (i.e., 0.5 degree MERRA-2 precipitation) is downscaled using a combination of topographic and stochastic downscaling methods (Daly et al. 1994; Nykanen and Harris, 2003). Other meteorological inputs such as near-surface air temperature, humidity, pressure, winds and longwave radiation are corrected for elevation through lapse-rate and hypometric adjustments. The incident shortwave radiation field is adjusted using a slope-aspect based terrain correction method. High-resolution parameter inputs of vegetation, albedo, Leaf Area Index (LAI) and albedo (from MODIS/VIIIRS at 500m – 1km resolution), elevation, slope and aspect (from Shuttle Radar Topography Mission; SRTM; from 30 m resolution), and soils (International Soil Reference and Information Centre; ISRIC; from 1km resolution) are employed in the model simulations.

## File Format

NetCDF 4

## File Naming:

```
LIS_HIST_YYYYMMDDHHNN.d01.nc
```

where YYYY is a 4-digit year, MM is a 2-digit month, DD is a 2-digit day, HH is a 2-digit hour, and NN is a 2-digit minute.

## Map projection and spatial coverage

Lat/Lon projection
Latitude: 22.025 – 38.975 N
Longitude: 66.025 – 84.975 E

## Variables

Output names generally follow the Assistance for Land-surface Modelling activities (ALMA) data exchange convention. Click [here](http://www.lmd.jussieu.fr/~polcher/ALMA/convention_output_3.html) to view the ALMA list of Standard Model Output. LIS output is a subset of that list.

# Known issues

There are known issues with snow related-products (e.g., snow temperature, snow ice, and snow density) that need to be solved.

# References

* Daly, C., R.P. Neilson and D.L. Phillips, 1994: A statistical-topographic model for mapping climatological precipitation over mountainous terrain, J. Appl. Meteor., 33(2), 140-158.

* Kumar , S.V., C.D. Peters-Lidard, Y. Tian, P.R. Houser, J. Geiger, S. Olden, L. Lighty, J.L.Eastman, B. Doty, P. Dirmeyer, J. Adams, K. Mitchell, E. F. Wood and J. Sheffield, 2006: Land Information System - An Interoperable Framework for High Resolution Land Surface Modeling. Environmental Modelling & Software, Vol.21, 1402-1415. DOI:10.1016/j.envsoft.2005.07.004

* Nykanen, D.K. and D. Harris, 2003: Orographic influences on the multiscale statistical properties of precipitation, J. Geophys. Res., 108(D8),8381,doi:10.1029/2001JD001518.

# Contacts

* Sujay Kumar
* Yeosang Yoon