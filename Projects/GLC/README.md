* Global Landslide Catalog Overview

The Global Landslide Catalog (GLC) lists rainfall-triggered mass movements from around the Earth. It was created at NASA GSFC by searching media reports and other sources for these events. This database is currently being updated by summer interns.

## Overview

| | |
|---:|:---- |
| Platform/Product | GLC / Point inventory |
| Gridded Resolution | N/A |
| Effective Resolution| N/A |
| Temporal Coverage | Jan. 2007 - Jul. 2016 |
| Temporal Resolution | N/A |
| Data Format | shapefile (.shp) |
| Version | 2.1 |

## Data Description

The GLC contains over 9,000 spatial points, each with descriptive attributes. In general, only locations with dates were recorded. A spatial accuracy estimate has been made for all points, based on the nature of the source material.

### Attribute fields

source_name,source_link,event_id,event_date,event_time,event_title,event_description,location_description,location_accuracy,landslide_category,landslide_trigger,landslide_size,landslide_setting,fatality_count,injury_count,storm_name,photo_link,comments,event_import_source,event_import_id,latitude,longitude,country_name,country_code,admin_division_name,admin_division_population,gazetteer_closest_point,gazetteer_distance,submitted_user,submitted_date,created_user,created_date,last_edited_user,last_edited_date

#### File Naming

```glc[date].[extension]```
date - the download date as YYYYMMDD.

extension - may be one of the following:
.shp (feature geometry)
.shx (shape index)
.dbf (text-based attributes)
.prj (coordinate system)
.sbx (spatial index)
.sbn (spatial index)
.cpg (identifies character encoding)
.shp.xml (XML metadata)

#### Projection

+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs

#### Spatial Coverage

Latitude bounds : N 90, N 90 (DDeg)
Longitude bounds: E -180, E 180 (DDeg)

## Data Access

### NASA ADAPT
* Datasets are located in the following folder on NASA ADAPT:

```
/att/pubrepo/hma_data/products/landslides
```

## Usage constraints

* data may be freely used or distributed, but citation is required

## Contact

* Thomas Stanley

## References

* Kirschbaum, D. B., Stanley, T., & Zhou, Y. (2015). Spatial and temporal analysis of a global landslide catalog. Geomorphology, 249, 4-15.

* Kirschbaum, D. B., Adler, R. F., Hong, Y., Hill, S., & Lerner-Lam A. (2010). A global landslide catalog for hazard applications: method, results, and limitations. Natural Hazards, 52(3), 561-575.