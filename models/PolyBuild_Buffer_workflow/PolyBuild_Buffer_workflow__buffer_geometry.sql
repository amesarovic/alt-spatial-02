{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH poly_build AS (

  SELECT * 
  
  FROM {{ ref('poly_build')}}

),

PolyBuild_1 AS (

  {{
    andre_spatial_09.PolyBuild(
      'poly_build', 
      'SequencePolygon', 
      'longitude', 
      'latitude', 
      'route_id', 
      'stop_schedule'
    )
  }}

),

buffer_geometry AS (

  {{
    andre_spatial_09.Buffer(
      'PolyBuild_1', 
      [
        { "name": "grouping_column_name", "dataType": "String" }, 
        { "name": "geometry_wkt", "dataType": "String" }
      ], 
      'geometry_wkt', 
      1, 
      'miles', 
      'output'
    )
  }}

)

SELECT *

FROM buffer_geometry
