# Coupled-Ocean-Wave-Sedimentation Transport Modeling System (COAWST) Version 3.2 (Revision 1147, March 2017)

HiMAT Point of Contact: stephen.d.nicholls@nasa.gov

## HiMAT COAWST Simulation Status
**Last Update: 19 July 2019 12:30 PM EDT**

| | | | | | |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| Model Simulation Name | Model Run Period | Run Status | Current Model Run Date | <sup>1</sup>Latest Date Available on ADAPT | % Complete |
| Water Year (2008) | 00 UTC 1 Oct. 2007 - 00 UTC 1 Oct. 2008 | FINISHED | 00 UTC 1 Oct. 2007 | 00 UTC 1 Oct. 2008 | 100.0% |
| Water Year (2015) | 00 UTC 1 Oct. 2014 - 00 UTC 1 Oct. 2015 | FINISHED | 00 UTC 1 Oct. 2015 | 00 UTC 1 Oct. 2015 | 100.0% |
| Historical Simulation (1999 - 2014) | 00 UTC 1 Oct. 1999 - 00 UTC 1 Oct. 2014 | RUNNING | 00 UTC 01 Nov 2011 | 23 UTC 30 Sept 2011 | 80.5% |
| Sentinel-1 Comparison | 00 UTC 15 Dec. 2017 - 00 UTC 1 Apr. 2018 | FINISHED | 00 UTC 1 Apr. 2018 | 00 UTC 1 Apr. 2018 | 100.0% |

ADAPT Data Location: /att/pubrepo/hma_data/HiMAT_COAWST_Output

<sup>1</sup> Data Available on ADAPT >> WRF: 1-hr, Daily, Monthly || ROMS: Daily, Monthly || WRF and ROMS 6-hr data are generated, but are too large to fit on ADAPT

## HiMAT COAWST Configuration
![alt text](https://github.com/NASA-Planetary-Science/HiMAT/blob/master/Projects/COAWST/WRF_1-2_Model_Domain_Map.png_HiMAT_HMA_Final.png)
**COAWST domain configration used for ocean-atmosphere coupled simulations. WRF (atmosphere) and ROMS (ocean) are run over the entire region at 20-km grid spacing (d01), but WRF also contains a nested grid (d02; black box) with 4-km grid spacing. Elevation data is in meters above mean sea level. For the atmospheric dataset there also exists "d021", which takes the 4-km data and degrades these data to 20-km grid spacing**

**Model Datafile Naming Convention <br/>
d01 = 20-km grid spacing, regional model grid (used for atmosphere "wrfout" and ocean "romsout" files) <br/>
d02 = 4-km grid spacing, convective resolving model grid focused on HMA region, atmosphere only <br/>
d021 = d02 data degraded to 20-km grid spacing of d01, atmosphere only <br/>** 


| | |
|:-----:|:-----:|
| **COUPLED OCEAN-ATMOSPHERE-WAVE-SEDIMENTION-TRANSPORT (COAWST) MODELLING SYSTEM SPECFIC SETTINGS** | 
| Model Version | Version 3.2, Revision 1147 (March 2017) |
| Coupling Option | WRF-ROMS | 
| Coupling Interval | 1800 seconds (30 minutes) | 
| Coupler | Model Coupling Toolkit (MCT) Version 2.6.0 |
| COAWST Model Project Page | https://woodshole.er.usgs.gov/operations/modeling/COAWST/ |
| COAWST Citation | Warner, J. C., B. Armstrong, R. He, and J. B. Zambon, 2010: Development of a Coupled Ocean-Atmosphere-Wave-Sediment Transport (COAWST) modeling system. Ocean Modelling, 35, 230–244 | 

| | |
|:-----:|:-----:|
| **WEATHER RESEARCH AND FORECASTING (WRF) MODEL SPECIFIC SETTINGS** | 
| Model Version | Version 3.7.1 |
| Model Description | Atmosphere model applying fully-compressible, non-hydrostatic, Eulerian equations in terrain following (sigma) coordinates |
| Map Projection | Lambert Conical Conformial | 
| Model Domains | 2 |
| Grid Resolution (domain) | 20 km, 4 km | 
| Vertical Levels | 61 | 
| Model top pressure | 1,000 Pa (10 hPa) |
| Time step | 25 seconds (20 km), 5 seconds (4 km) |
| Historical Input Data | Modern Era Retrospective-analysis for Research and Applications, 2nd Version (MERRA-2) | 
| Future Input Data | Global Climate Model (TBD) | 
| Data input interval | 180 minutes |
| Boundary update interval | 180 minutes |
| Data Output Frequency | 1 hr, 6 hr, Daily, Monthly |
| Model Parameterization | Boundary Layer: YSU Scheme |
|| Cumulus: Multi-scale Kain-Fritsch Scheme 
|| Land Surface: NOAH-MP |
|| Microphysics: Goddard Cumulus Ensemble (GCE) - 4ice |
|| Radiation (Long Wave): RRTM |
|| Radiation (Short Wave): RRTMG |
|| Surface Scheme: Revised MM5 Monin-Obukhov |

| | |
|:-----:|:-----:|
| **REGIONAL OCEAN MODELING SYSTEM (ROMS) SPECIFIC SETTINGS** | 
| Model Version | Subversion 797 |
| Model Desciption | Ocean model applying 3D Reynolds-averaged Navier–Stokes equations using hydrostatic and Boussinesq approximations in terrain following (sigma) coordinates|
| Map Projection | Lambert Conical Conformial | 
| Model Domains | 1 |
| Grid Resolution (domain) | 20 km | 
| Vertical Levels | 16 | 
| Time step | 6 seconds |
| Historical Input Data | Hybrid Coordinate Ocean Model (HYCOM) |
| Future Input Data | Global Climate Model (TBD) | 
| Data input interval | 1440 minutes (1 day) |
| Boundary update interval | 1440 minutes (1 day)
| Data Output Frequency | 6 hr, Daily, Monthly |
| ROMS Parameterization | Centered vertical advection: 4th order |
|| Generic length scale mixing: On
|| Horizonal momentum mixing type: Constant sigma surfaces
|| Lateral Boundaries (W, S, E, N): Open, Open, Open, Closed |
|| T & S 3rd order upstream advection: On
|| T & S Harmonic horizonal mixing: On
|| Tidal elevation: Imposed
|| U & V Advection: On
|| U & V Coriolis: On
|| U & V Harmonic horizontal mixing: On
|| U & V Linear Bottom Friction: Off








