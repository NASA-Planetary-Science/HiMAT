## Key Details

| | | 
|:-----|:-----|
| Purpose of this file | Detail available WRF model output from COAWST simulations and its temporal availability |
| Dataset generation status | Please see "coawst_readme.md" for details |
| Output data format | NetCDF |

## Variable Descriptions and Time Frequencies

| | | | | | | | |
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| **WRF Name** | **Description** | **Units** | **Dims** |  **1 hr** | **6 hr** | **Daily** | **Monthly** |
| T2 | 2-m air temperature | K | x, y, t | X | X | X | X |
| RH2 | 2-m relative humidity | % | x, y, t |   |   | X | X |
| Q2 | 2-m specific humidity | Kg Kg<sup>-1</sup> | x, y, t | X | X | X | X |
| U10 | 10-m zonal wind speed | m s<sup>-1</sup> | x, y, t | X | X | X | X |
| V10 | 10-m meridional wind speed | m s<sup>-1</sup> | x, y, t | X | X | X | X |
| CLDFRA | Cloud fraction | none | x, y, z, t | X  | X |  |  |
| DATE | Date and Time of data | time | t |  |   | X | X |
| HGT | Land surface height | m | x, y | X | X | X | X |
| LANDMASK | Landmask (1 = Land, 0 = Ocean) | none | x, y | X  | X |  |  |
| LMASK | Landmask (1 = Land, 0 = Ocean) | none | x, y |  |   | X | X |
| GRAUPEL | Liquid-equivalent accumulated graupel | mm | x, y, t |   |   | X | X |
| GRAUPELNC* | Liquid-equivalent accumulated graupel (explcit) | mm | x, y, t | X | X |  |  |
| HAILNC* | Liquid-equivalent accumulated hail (explcit) | mm | x, y, t | X | X |  |  |
| PRECIP | Liquid-equivalent accumulated precipiation | mm | x, y, t |  |   | X | X |
| RAINC** | Liquid-equivalent accumulated precipiation (convective parameterization) | mm | x, y, t | X | X |  |  |
| RAINNC** | Liquid-equivalent accumulated precipiation (explicit) | mm | x, y, t | X | X |  |  |
| RAIN | Liquid-equivalent accumulated rainfall | mm | x, y, t |  |   | X | X |
| SNOW | Liquid-equivalent accumulated snowfall | mm | x, y, t |  |   | X | X |
| SNOWC* | Liquid-equivalent accumulated snowfall (convective parameterization) | mm | x, y, t | X | X |  |  |
| SNOWNC* | Liquid-equivalent accumulated snowfall (explicit) | mm | x, y, t | X | X |  |  |
| PSFC | Surface pressure | Pa | x, y, t | X | X |  |  |
| LAT | Unstaggered latitude | °N | x, y |  |   | X | X |
| XLAT | Unstaggered latitude | °N | x, y | X  | X  |  |  |
| LON | Unstaggered longitude | °E | x, y |  |   | X | X |
| XLONG | Unstaggered longitude | °E | x, y | X | X  |  |  |

*WRF precipitation type variable. Shown data is accumulated from model initialization. Total model-simulated precipiation adds the explicitly simualted (NC) and convective parameterization (C) components

**WRF total precipitation type variable. This variable shows total precipitation from all types of precipitation. To extract rainfall only, please subtract all other types of precipitation from the RAINC+RAINNC 

