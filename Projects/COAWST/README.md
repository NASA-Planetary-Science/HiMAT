# Coupled-Ocean-Wave-Sedimentation Transport Modeling System (COAWST) Version 3.2 (Revision 1147, March 2017)

HiMAT Point of Contact: stephen.d.nicholls@nasa.gov

## HiMAT COAWST Simulation Status
**Last Update: 1 June 2018 15:32 EST**

| | | | | |
|:-----:|:-----:|:-----:|:-----:|:-----:|
| Model Simulation Name | Model Run Period | Run Status | Current Model Run Date | Latest Date Available on ADAPT |
| Water Year (2008) | 00 UTC 1 Oct. 2007 - 00 UTC 1 Oct. 2008 | FINISHED | 00 UTC 1 Oct. 2007 | 00 UTC 1 Oct. 2008 |
| Water Year (2015) | 00 UTC 1 Oct. 2014 - 00 UTC 1 Oct. 2015 | FINISHED | 00 UTC 1 Oct. 2015 | 00 UTC 1 Oct. 2015 |
| Historical Simulation (1999 - 2015) | 00 UTC 1 Oct. 1999 - 00 UTC 1 Oct. 2015 | RUNNING | 12 UTC 30 June 2003 | N/A |
| Future Climate Simulation (15-year period) | TBD | Awaiting GCM input data | N/A | N/A |

## HiMAT COAWST Configuration
![alt text](https://github.com/NASA-Planetary-Science/HiMAT/blob/master/Projects/COAWST/WRF_1-2_Model_Domain_Map.png_HiMAT_HMA_Final.png)
**COAWST domain configration used for ocean-atmosphere coupled simulations. WRF (atmosphere) and ROMS (ocean) are run over the entire region at 20-km grid spacing, but WRF also contains a nested grid (black box) with 4-km grid spacing. Elevation data is in meters above mean sea level.**


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
| Time step | 40 seconds (20 km), 8 seconds (4 km) |
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
| Time step | 10 seconds |
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








