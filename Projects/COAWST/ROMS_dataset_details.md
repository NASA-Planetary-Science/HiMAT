## Key Details

| | |
|:-----|:-----|
| Purpose of this file | Detail available ROMS model output from COAWST simulations and its temporal availability |
| Dataset generation status | Please see "coawst_readme.md" for details |
| Output data format | NetCDF |


## Time Varying Variable Descriptions and Time Frequencies

| | | | | | | | |
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| **Variable Name** | **WRF Variable Name** | **Units** | **Dims** | **Staggered** | **6 hr** | **Daily** | **Monthly** 

| Ocean Water Velocity (Meridional) | v | m s-1 | x, y, z, t | yes, v | X | X | X |
| Ocean Water Velocity (Vertical) | w | m s-1 | x, y, z, t | yes, z | X | X | X |
| Ocean Water Velocity (Zonal) | u | m s-1 | x, y, z, t | yes, u | X | X | X |
| Salinity | salt | PSU | x, y, z, t | no | X | X | X |
| Sea Surface Height | zeta | m | x, y, t | no | X | X | X |
| Temperature | temp | Celsius | x, y, z, t | no | X | X | X |
| Time Since ROMS Model Initialization | ocean_time | s | t | no | X | X | X | 
| Vertically Integrated Water Velocity (Meridional) | vbar | m s-1 | x, y, t | no | X | X | X |
| Vertically Integrated Water Velocity (Zonal) | ubar | m s-1 | x, y, t | no | X | X | X |


## Time Invariant Variable Descriptions

| | | | 
|:-----|:-----|:-----|
| **ROMS Name** | **Description** | **Units** |
| h | bathymetry | m |
| f | Coriolis parameter | s<sup>-1</sup>|
| lat_psi | latitude for cross-staggered grid | °N | 
| lat_rho | latitude for unstaggered grid | °N |
| lat_rho | latitude for u-staggered grid | °N |
| lat_rho | latitude for v-staggered grid | °N |
| lon_psi | longitude for cross-staggered grid | °E |
| lon_rho | longitude for unstaggered grid | °E |
| lon_rho | longitude for u-staggered grid | °E |
| lon_rho | longitude for v-staggered grid | °E |
| mask_psi | land mask for cross-staggered grid (0 = land, 1 = ocean ) | none |
| mask_rho | land mask for unstaggered grid (0 = land, 1 = ocean ) | none |
| mask_rho | land mask for u-staggered grid (0 = land, 1 = ocean ) | none |
| mask_rho | land mask for v-staggered grid (0 = land, 1 = ocean ) | none |




| | | | | | |
|:-----|:-----|:-----|:-----|:-----|:-----|
| **ROMS Name** | **Description** | **Units** |  **6 hr** | **Daily** | **Monthly** |

