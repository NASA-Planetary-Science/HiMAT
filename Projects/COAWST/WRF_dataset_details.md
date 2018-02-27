## Key Details

| | | 
|:-----|:-----|
| Purpose of this file | Detail available WRF model output from COAWST simulations and its temporal availability |
| Dataset generation status | Please see "coawst_readme.md" for details |
| Output data format | NetCDF |
| Data notes | 1-hr and 6-hr data are instantaneous, daily and monthly data are averages or accumulations during the indicated period |

## Variable Descriptions and Time Frequencies

| | | | | | | | | |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| **Variable Name** | **WRF Variable Name** | **Units** | **Dims** | **Staggered** | **1 hr** | **6 hr** | **Day** | **Month** 
| <sup>1</sup> Accumulated Graupel (Liq Eq.) | ACCGRAUPEL | mm | x, y, t | no |  |  | X | X |
| <sup>1</sup> Accumulated Hail (Liq Eq.) | ACCHAIL | mm | x, y, t | no |  |  | X | X |
| <sup>1</sup> Accumulated Precipitation (Liq Eq.) | ACCPRECIP | mm | x, y, t | no |  |  | X | X |
| <sup>1</sup> Accumulated Rainfall | ACCRAIN | mm | x, y, t | no |  |  | X | X |
| <sup>1</sup> Accumulated Snowfall (Liq Eq.) | ACCSNOW | mm | x, y, t | no |  |  | X | X |
| Air Temperature | T | K | x, y, z, t | no |  | X |  |  |
| Air Temperature at 2m | T2 | K | x, y, t | no | X | X | X | X |
| Air Pressure | P | Pa | x, y, z, t | no |  | X |  |  |
| Albedo | ALBEDO | unitless | x, y, t | no |  | X |  |  |
| Background Albedo | ALBBCK | unitless | x, y, t | no |  | X |  |  |
| Cloud Fraction | CLDFRA | unitless| x, y, z, t | no |  | X |  |  |
| Composite Radar Reflectivity | COMDBZ | dBZ | x, y, t | no | X | X |  |  |
| Canopy Fraction Wetted or Snowed | FWET | unitless | x, y, t | no |  | X |  |  |
| Coriolis Cosine Latitude Term | E | s<sup>-1</sup> | x, y, t | no |  | X |  |  |
| Coriolis Sine Latitude Term | F | s<sup>-1</sup> | x, y, t | no |  | X |  |  |
| Cosine of Local Map Rotation | COSALPHA | unitless | x, y, t | no |  | X |  |  |
| Cosine of Local Solar zenith Angle | COSZEN | unitless | x, y, t | no |  | X |  |  |
| <sup>2</sup> Daily Averaged Winds (X-dir) at 10m | DAYU10 | m s<sup>-1</sup> | x, y, t | no |  |  | X |  |
| <sup>2</sup> Daily Averaged Winds (Y-dir) at 10m | DAYV10 | m s<sup>-1</sup> | x, y, t | no |  |  | X |  |
| Depth Centers of Soil Levels | ZS | m | z, t | no |  | X |  |  |
| Downward Longwave Flux at Ground | SWDOWN | W m<sup>-2</sup> | x, y, t | no | X | X | X | X |
| Downward Shortwave Flux at Ground | GLW | W m<sup>-2</sup> | x, y, t | no | X | X | X | X |
| Dry Air Mass (Perturbation) in Column | MU | Pa | x, y, t | no |  | X |  |  |
| Dry Air Mass (Base) in Column | MUB | Pa | x, y, t | no |  | X |  |  |
| Eta Model Grid Values on Half Levels | ZNU | unitless | z, t | no |  | X |  |  |
| Eta Model Grid Values on Full Levels | ZNW | unitless | z, t | yes, z |  | X |  |  |
| Fraction Frozen Precipitation | SR | unitless | x, y, t | no |  | X |  |  |
| Geopotential | PH | m<sup>2 </sup> s<sup>-2</sup> | x, y, z, t | yes, z |  | X |  |  |
| Ground Heat Flux | GRDFLX | W m<sup>-2</sup> | x, y, t | no |  | X |  |  |
| Ground Water Storage | WT | mm | x, y, t | no |  | X |  |  |
| Landmask | LANDMASK | unitless | x, y, t | no | X | X | X | X |
| Landuse Use Category | LU_INDEX | unitless | x, y, t | no |  | X |  |  |
| Latent Heat Flux at Surface | LH | W m<sup>-2</sup> | x, y, t | no | X | X | X | X |
| Latitude | XLAT | °N | x, y, t | no | X | X | X | X | 
| Latitude U Stag | XLAT_U | °N | x, y, t | yes, u |  | X |  |  | 
| Latitude V Stag | XLAT_V | °N | x, y, t | yes, v |  | X |  |  | 
| Longitude | XLONG | °E | x, y, t | no | X | X | X | X | 
| Longitude U Stag | XLONG_U | °E | x, y, t | yes, u |  | X |  |  | 
| Longitude V Stag | XLONG_V | °E | x, y, t | yes, v |  | X |  |  | 
| Map Factor, Mass Grid | MAPFAC_M | unitless | x, y, t | no |  | X |  |  |
| Map Factor, Mass Grid, X-dir | MAPFAC_MX | unitless | x, y, t | no |  | X |  |  |
| Map Factor, Mass Grid, Y-dir | MAPFAC_MY | unitless | x, y, t | no |  | X |  |  |
| Map Factor, U Grid | MAPFAC_U | unitless | x, y, t | yes, u |  | X |  |  |
| Map Factor, U Grid, X-dir | MAPFAC_UX | unitless | x, y, t | yes, u |  | X |  |  |
| Map Factor, U Grid, Y-dir | MAPFAC_UY | unitless | x, y, t | yes, u |  | X |  |  |
| Map Factor, V Grid | MAPFAC_V | unitless | x, y, t | yes, v |  | X |  |  |
| Map Factor, V Grid, X-dir | MAPFAC_VX | unitless | x, y, t | yes, v |  | X |  |  |
| Map Factor, V Grid, Y-dir | MAPFAC_VY | unitless | x, y, t | yes, v |  | X |  |  |
| Mixing Ratio (Graupel) | QGRAUPEL | kg kg<sup>-1</sup> | x, y, z, t | no |  | X |  |  | 
| Mixing Ratio (Hail) | QHAIL | kg kg<sup>-1</sup> | x, y, z, t | no |  | X |  |  | 
| Mixing Ratio (Ice) | QICE | kg kg<sup>-1</sup> | x, y, t | no |  | X |  |  | 
| Mixing Ratio (Rain) | QRAIN | kg kg<sup>-1</sup> | x, y, z, t | no |  | X |  |  | 
| Mixing Ratio (Snow) | QSNOW | kg kg<sup>-1</sup> | x, y, z, t | no |  | X |  |  | 
| <sup>2</sup> Monthly Averaged Winds (X-dir) at 10m | MONU10 | m s<sup>-1</sup> | x, y, t | no |  |  |  | X |
| <sup>2</sup> Monthly Averaged Winds (Y-dir) at 10m | MONV10 | m s<sup>-1</sup> | x, y, t | no |  |  |  | X |
| Monthly Averaged Water Vapor Mixing Ratio at 2m | MONQ2 | K | x, y, t | no |  |  |  | X |
| Net Shortwave at Surface | GSW | W m<sup>-2</sup> | x, y, t | no | X | X | X | X |
| Outgoing Longwave Radition (TOA) | OLR | W m<sup>-2</sup> | x, y, t | no | X | X | X | X |
| Planetary Boundary Layer Height | PBLH | m | x, y, t | no | X | X | X | X |
| Potential Temperature at 2m | TH2 | K | x, y, t | no |  | X |  |  |
| Pressure at Model Top | P_TOP | Pa | x, y, t | no |  | X |  |  |
| Relative Humidity at 2m | RH2 | % | x, y, t | no | X | X | X | X | 
| Sea Ice Flag | SEAICE | unitless | x, y, t | no |  | X |  |  |
| Sea Surface Temperature | SST | K | x, y, t | no |  | X |  |  |
| Sine of local map rotation | SINALPHA | unitless | x, y, t | no |  | X |  |  |
| Snow Coverage | SNOWC | unitless | x, y, t | no | X | X | X | X | 
| Snow Height | SNOWH | m | x, y, t | no | X | X | X | X |
| Soil Temperature | TSLB | K | x, y, z, t | no |  | X |  |  |
| Soil Moisture | SMOIS | m<sup>3</sup> m<sup>-3</sup> | x, y, z, t | no |  | X |  |  |
| Surface Emissivity | EMISS | unitless | x, y, t | no |  | X |  |  |
| Surface Runoff | SFROFF | mm | x, y, t | no |  | X |  |  |
| Surface Pressure | PSFC | Pa | x, y, t | no | X | X | X | X |
| Surface Skin Temperature | TSK | K | x, y, t | no |  | X |  |  |
| Terrain Height | XLONG | m | x, y, t | no | X | X | X | X | 
| Mixing Ratio (Rain) | QRAIN | kg kg<sup>-1</sup> | x, y, z, t | no |  | X |  |  | 
| Total Cloud Fraction | TOTCLDFRAC | unitless | x, y, t | no | X | X | X | X |
| <sup>1</sup> Total Accumulated Graupel (Liq Eq.) | TOTGRAUPEL | mm | x, y, t | no | X | X |  |  |
| <sup>1</sup> Total Accumulated Hail (Liq Eq.) | TOTHAIL | mm | x, y, t | no | X | X |  |  |
| <sup>1</sup> Total Accumulated Precipitation (Liq Eq.) | TOTPRECIP | mm | x, y, t | no | X | X |  |  |
| <sup>1</sup> Total Accumulated Rainfall | TOTRAIN | mm | x, y, t | no | X | X |  |  |
| <sup>1</sup> Total Accumulated Snowfall (Liq Eq.) | TOTSNOW | mm | x, y, t | no | X | X |  |  |
| Upward Heat Flux at Surface | HFX | W m<sup>-2</sup> | x, y, t | no | X | X | X | X |
| Upward Moisture Flux at Surface | QFX | kg m<sup>-2</sup> s<sup>-1</sup> | x, y, t | no | X | X | X | X |
| Underground Runoff | UDROFF | mm | x, y, t | no |  | X |  |  |
| Vegetative Fraction | FVEG | unitless | x, y, t | no |  | X |  |  |
| Vegetation Fraction | VEGFRA | unitless | x, y, t | no |  | X |  |  |
| Water in Aquifer | WA | mm | x, y, t | no |  | X |  |  |
| Water Table Depth | ZWT | m | x, y, t | no |  | X |  |  |
| Water Vapor Mixing Ratio at 2m | Q2 | kg kg<sup>-1</sup> | x, y, z, t | no | X | X | X | X |
| Water Vapor Mixing Ratio | QVAPOR | kg kg<sup>-1</sup> | x, y, t | no |  | X |  |  |
| <sup>2</sup> Wind (X-dir) at 10 m | U10 | m s<sup>-1</sup> | x, y, t | no | X | X | X | X |
| <sup>2</sup> Wind (X-dir) | U | m s<sup>-1</sup> | x, y, z, t | yes, u |  | X |  |  |
| <sup>2</sup> Wind (Y-dir) at 10 m | V10 | m s<sup>-1</sup> | x, y, t | no | X | X | X | X |
| <sup>2</sup> Wind (Y-dir) | V |m s<sup>-1</sup> | x, y, z, t | yes, v |  | X |  |  |
| Wind (Vertical) | W | m s<sup>-1</sup> | x, y, z, t | yes, z |  | X |  |  |

<sup>1</sup> All total accumulations are relative to the model simulation initalization time (see COAWST readme for date)

<sup>2</sup> Winds generated by WRF are grid-relative. To calculate Earth-relative winds, you will need to apply the following conversion formula: Uearth = Umodel x COSALPHA + Vmodel x SINALPHA; Vearth = Vmodel x COSALPHA + Umodel x SINALPHA 
