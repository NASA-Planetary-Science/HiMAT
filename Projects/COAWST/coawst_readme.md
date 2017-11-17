# Coupled-Ocean-Wave-Sedimentation Transport Modeling System (COAWST) Version 3.2 (Revision 1147, March 2017)

Modeling System Citation:  Warner, J. C., B. Armstrong, R. He, and J. B. Zambon, 2010: Development of a Coupled Ocean-Atmosphere-Wave-Sediment Transport (COAWST) modeling system. Ocean Modelling, 35, 230–244

HiMAT Point of Contact: stephen.d.nicholls@nasa.gov

## HiMAT COAWST Configuration

| | |
|:-----|:-----|
| OVERALL COAWST SETTINGS | 
| Coupling Option | WRF-ROMS | 
| Coupling Interval | 1800 seconds (30 minutes) | 
| Coupler | Model Coupling Toolkit (MCT) Version 2.6.0 |
| COAWST Citation | Warner, J. C., B. Armstrong, R. He, and J. B. Zambon, 2010: Development of a Coupled Ocean-Atmosphere-Wave-Sediment Transport (COAWST) modeling system. Ocean Modelling, 35, 230–244 | 

| | |
|:-----|:-----|
| WRF SPECIFIC SETTINGS | 
| Model Version | Version 3.7.1 |
| Map Projection | Lambert Conical Conformial | 
| Model Domains | 2 |
| Grid Resolution (domain) | 20 km, 5 km | 
| Vertical Levels | 61 | 
| Vertical Coordinate System | Sigma (Terrain following) |
| Model top pressure | 1,000 Pa |
| Time step | 40 seconds |
| Input Data | Modern Era Retrospective-analysis for Research and Applications, 2nd Version (MERRA-2) | 
| Data input interval | 180 minutes |
| Boundary update interval | 180 minutes |

| | |
|:-----|:-----|
| ROMS SPECIFIC SETTINGS | 
| Model Version | Subversion 797 |
| Map Projection | Lambert Conical Conformial | 
| Model Domains | 1 |
| Grid Resolution | 20 km | 
| Vertical Levels | 16 | 
| Vertical Coordinate System | Sigma (Bathymetry following) |
| Time step | 10 seconds |
| Model input | Hybrid Coordinate Ocean Model (HYCOM) |
| Data input interval | 1440 minutes (1 day) |
| Boundary update interval | 1440 minutes (1 day)






