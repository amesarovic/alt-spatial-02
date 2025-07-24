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

build_polyline AS (

  {{
    andre_spatial_09.PolyBuild(
      'poly_build', 
      'SequencePolyline', 
      'longitude', 
      'latitude', 
      'route_id', 
      'stop_schedule'
    )
  }}

)

SELECT *

FROM build_polyline
