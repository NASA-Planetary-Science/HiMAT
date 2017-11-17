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
| f | Coriolis parameter | s<sup>-1</sup>|
| h | bathymetry | m |
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


## Time Varying Variable Descriptions and Time Frequencies

| | | | | | |
|:-----|:-----|:-----|:-----|:-----|:-----|
| **ROMS Name** | **Description** | **Units** |  **6 hr** | **Daily** | **Monthly** |
| ocean_time | time since ROMS model initialization | s | | | |
| temp | potential temperature | Celsius | X | X | X |
| salt | salinity | psu | X | X | X |
| w | upward sea velocity | m s<sup>-1</sup> | X | X | X |
| u | u-momentum | m s<sup>-1</sup> | X | X | X |
| ubar | vertically integrated u-momentum | m s<sup>-1</sup> | X | X | X |
| v | v-momentum | m s<sup>-1</sup> | X | X | X |
| vbar | vertically integrated v-momentum | m s<sup>-1</sup> | X | X | X |
| zeta | sea surface height | m | X | X | X |
| zob | bottom roughtness | m | X | X | X |
| zos | surface roughness | m | X | X | X |
