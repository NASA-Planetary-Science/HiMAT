# Coupled-Ocean-Wave-Sedimentation Transport Modeling System (COAWST) Version 3.2 (Revision 1147, March 2017)

## COAWST Component Model Details 

| | | |
|:-----|:-----|:-----|
| Atmosphere | Weather Research and Forecasting model (WRF) | Version 3.7.1 |
| Ocean | Regional Ocean Modeling System model (ROMS) | Revision 797 |
| Wave | Simulating Waves Nearshore model (SWAN) | Version 41.01AB|
| Sedimentation transport | Community Sediment Transport Modeling System (CSTMS) | N/A |
| Coupler | Model Coupling Toolkit (MCT) | Version 2.6.0 |
| Weighted Interpolation | Spherical Coordinate Interpolating Package (SCRIP) |
| Citation | Warner, J. C., B. Armstrong, R. He, and J. B. Zambon, 2010: Development of a Coupled Ocean-Atmosphere-Wave-Sediment Transport (COAWST) modeling system. Ocean Modelling, 35, 230–244 | |

## HiMAT Specific Model Run Configuration

| | | |
|:-----|:-----|:-----|
| Coupling Option | WRF-ROMS | Version 3.7.1 |
| Coupling Interval | 1800 seconds (30 minutes) |
| | | 
| WRF Configuration Details | |
| Map Projection | Lambert Conical Conformial | |
| Model Domains | 2 |
| Model Resolution | D1: 20, D2: 5 | |

| Wave | Simulating Waves Nearshore model (SWAN) | Version 41.01AB|
| Sedimentation transport | Community Sediment Transport Modeling System (CSTMS) | N/A |
| Coupler | Model Coupling Toolkit (MCT) | Version 2.6.0 |
| Weighted Interpolation | Spherical Coordinate Interpolating Package (SCRIP) | N/A |



| | | 
|:-----|:-----|
|Model Version|WRF 3.8.1|
|Point of contact |adam.kochanski@utah.edu|
| | |
| MAP AND GRIDS | |
| Map projection | lambert conformal |
| Number of vertical layers | 45  |
| Horizontal grid spacing | 36km/12km/4km/(1.33km) |
| Static geographic fields | standard geog 3.8.1 input |
| | |
| TIMING | |
| Simulation period | 2000, 2001, 2002, 2008 |
| Time step | 120s / 60s (for summer months with strong convection) |
| | |
| NESTING STRATEGY |  | 
| Nesting | 1-way, 3:1 ratio  |
| | |
| FORCING STRATEGY | |
| Boundary conditions | CFSR |
| Sea surface temperature | CFSR  |
| Initializiation | CFSR | 
| Runs starting time | 2000-01-01:00:00 |
| Runs duration | 1 month (31 days) per 1 run | 
| Spinup | 1-year  |
| | |
| PHYSICAL PARAMETERIZATION SCHEMES | | 
| Shortwave radiation | MM5 (Dudhia)  |
| Longwave radiation | RRTM  |
| Cumulus parameterization | Betts-Miller-Janjic (only 36km and 12km domains) |
| Microphysics | Thompson / Goddard 6-class  | 
| Land surface model | Noah MP  | 
| PBL | YSU  |
