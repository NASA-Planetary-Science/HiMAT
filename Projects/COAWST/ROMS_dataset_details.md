## Key Details

| | |
|:-----|:-----|
| Purpose of this file | Detail available ROMS model output from COAWST simulations and its temporal availability |
| Dataset generation status | Please see "coawst_readme.md" for details |
| Output data format | NetCDF |



## Time Invariant Variable Descriptions

| | | | 
|:-----|:-----|:-----|
| **ROMS Name** | **Description** | **Units** |
| bathymetry | h | m |
| Coriolis Parameter | f | s-1|
| Latitude for cross-staggered grid | lat_psi | °N | 
| Latitude for unstaggered grid | lat_rho | °N |
| Latitude for u-staggered grid | lat_u | °N |
| Latitude for v-staggered grid | lat_v | °N |
| Longitude for cross-staggered grid | lon_psi |  °E |
| Longitude for unstaggered grid | lon_rho | °E |
| Longitude for u-staggered grid | lon_u | °E |
| Longitude for v-staggered grid | lon_v | °E |
| Land Mask for Cross-staggered grid (0 = land, 1 = ocean ) | mask_psi |  none |
| Land Mask for Unstaggered Grid (0 = land, 1 = ocean ) | mask_rho | none |
| Land Mask for U-staggered Grid (0 = land, 1 = ocean ) | mask_u | none |
| Land Mask for V-staggered Grid (0 = land, 1 = ocean ) | mask_v | none |


## Time Varying Variable Descriptions and Time Frequencies

| | | | | | | | |
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| **Variable Name** | **ROMS Variable Name** | **Units** | **Dims** | **Staggered** | **6 hr** | **Daily** | **Monthly** |
| Ocean Water Velocity (Meridional) | v | m s-1 | x, y, z, t | yes, v | X | X | X |
| Ocean Water Velocity (Vertical) | w | m s-1 | x, y, z, t | yes, z | X | X | X |
| Ocean Water Velocity (Zonal) | u | m s-1 | x, y, z, t | yes, u | X | X | X |
| Salinity | salt | PSU | x, y, z, t | no | X | X | X |
| Sea Surface Height | zeta | m | x, y, t | no | X | X | X |
| Temperature | temp | Celsius | x, y, z, t | no | X | X | X |
| Time Since ROMS Model Initialization | ocean_time | s | t | no | X | X | X | 
| Vertically Integrated Water Velocity (Meridional) | vbar | m s-1 | x, y, t | no | X | X | X |
| Vertically Integrated Water Velocity (Zonal) | ubar | m s-1 | x, y, t | no | X | X | X |
