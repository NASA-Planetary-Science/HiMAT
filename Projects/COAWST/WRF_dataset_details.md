## Key Details

| | | 
|:-----|:-----|
| Purpose of this file | Detail available WRF model output from COAWST simulations and its temporal availability |
| Dataset generation status | Please see "coawst_readme.md" for details |
| Output data format | NetCDF |

## Variable Descriptions and Time Frequencies

| | | | | | | |
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| **WRF Name** | **Description** | **Units** |  **1 hr** | **6 hr** | **Daily Avg/Accum** | **Monthly Avg/Accum** |
| T2 | 2-m air temperature | K | X | X | X | X |
| RH2 | 2-m relative humidity | % |   |   | X | X |
| Q2 | 2-m specific humidity | Kg Kg<sup>-1</sup> | X | X | X | X |
| CLDFRA | Cloud fraction | none | X  | X |  |  |
| DATE | Date and Time of data | yyyy-mm-dd hh:mm:ss format |   |   | X | X |
| HGT | Land surface height | m | X | X | X | X |
| LANDMASK | Landmask (1 = Land, 0 = Ocean) | none | X  | X |  |  |
| LMASK | Landmask (1 = Land, 0 = Ocean) | none |   |   | X | X |
| GRAUPEL | Liquid-equivalent accumulated graupel | mm |   |   | X | X |
| GRAUPELNC* | Liquid-equivalent accumulated graupel (explcit) | mm | X | X |  |  |
| HAILNC* | Liquid-equivalent accumulated hail (explcit) | mm | X | X |  |  |
| PRECIP | Liquid-equivalent accumulated precipiation | mm |   |   | X | X |
| RAINC* | Liquid-equivalent accumulated precipiation (convective parameterization) | mm | X | X |  |  |
| RAINNC* | Liquid-equivalent accumulated precipiation (explicit) | mm | X | X |  |  |
| RAIN | Liquid-equivalent accumulated rainfall | mm |   |   | X | X |
| SNOW | Liquid-equivalent accumulated snowfall | mm |   |   | X | X |
| SNOWC* | Liquid-equivalent accumulated snowfall (convective parameterization) | mm | X | X |  |  |
| SNOWNC* | Liquid-equivalent accumulated snowfall (explicit) | mm | X | X |  |  |
| LAT | Unstaggered latitude | °N |   |   | X | X |
| XLAT | Unstaggered latitude | °N | X  | X  |  |  |
| LON | Unstaggered longitude | °E |   |   | X | X |
| XLONG | Unstaggered longitude | °E |  X | X  |  |  |

"*WRF precipitation type variable. Shown data is accumulated from model initialization. Total model simulated precipiation adds the convective and convective parameterization" 

"**WRF total precipitation type variable. This variable shows total precipitation from all types of precipitation. To extract rainfall only, please subtract all other types of precipitation from the RAINC+RAINNC" 

