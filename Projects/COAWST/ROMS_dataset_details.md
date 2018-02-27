## Key Details

| | |
|:-----|:-----|
| Purpose of this file | Detail available ROMS model output from COAWST simulations and its temporal availability |
| Dataset generation status | Please see "coawst_readme.md" for details |
| Output data format | NetCDF |



## Time Invariant Variable Descriptions

| | | | |
|:-----|:-----|:-----|:-----|
| **ROMS Name** | **Description** | **Units** | **Staggered** |
| bathymetry | h | m | no |
| Coriolis Parameter | f | s-1| no | 
| Latitude for cross-staggered grid | lat_psi | °N | yes, psi |  
| Latitude for unstaggered grid | lat_rho | °N | no | 
| Latitude for u-staggered grid | lat_u | °N | yes, u | 
| Latitude for v-staggered grid | lat_v | °N | yes, v |
| Longitude for cross-staggered grid | lon_psi |  °E | yes, psi |
| Longitude for unstaggered grid | lon_rho | °E | no |
| Longitude for u-staggered grid | lon_u | °E | yes, u |
| Longitude for v-staggered grid | lon_v | °E | yes, v |
| Land Mask for Cross-staggered grid (0 = land, 1 = ocean ) | mask_psi |  none | yes, psi |
| Land Mask for Unstaggered Grid (0 = land, 1 = ocean ) | mask_rho | none | no |
| Land Mask for U-staggered Grid (0 = land, 1 = ocean ) | mask_u | none | yes, u | 
| Land Mask for V-staggered Grid (0 = land, 1 = ocean ) | mask_v | none | yes, v  |
| S-Coordinate at Rho-points | s_rho | none | no |
| S-Coordinate at W-points | s_w | none | yes, z |
| S-Coordinate Stretching at Rho-points | Cs_r | none | no |
| S-Coordinate Streteching at W-points | Cs_w | none | yes, z |


## Time Varying Variable Descriptions and Time Frequencies

| | | | | | | | |
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| **Variable Name** | **ROMS Variable Name** | **Units** | **Dims** | **Staggered** | **6 hr** | **Daily** | **Monthly** |
| Ocean Water Velocity (Meridional) | v | m s-1 | x, y, z, t | yes, v | X | X | X |
| Ocean Water Velocity (Vertical) | w | m s-1 | x, y, z, t | yes, z | X | X | X |
| Ocean Water Velocity (Zonal) | u | m s-1 | x, y, z, t | yes, u | X | X | X |
| S-coordinate Vertical Momentum Component | omega | m s-1 | x, y, z, t | yes, z | X | X | X |
| Salinity | salt | PSU | x, y, z, t | no | X | X | X |
| Sea Surface Height | zeta | m | x, y, t | no | X | X | X |
| Temperature | temp | Celsius | x, y, z, t | no | X | X | X |
| Time Since ROMS Model Initialization | ocean_time | s | t | no | X | X | X | 
| Vertically Integrated Water Velocity (Meridional) | vbar | m s-1 | x, y, t | no | X | X | X |
| Vertically Integrated Water Velocity (Zonal) | ubar | m s-1 | x, y, t | no | X | X | X |

*NOTE1: Time variables in ROMS are in seconds after model initialization, please see COAWST readme for initialization date.
