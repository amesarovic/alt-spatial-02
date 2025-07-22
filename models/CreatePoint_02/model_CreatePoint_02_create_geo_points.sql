{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdez5aun__CreatePoint_02__create_geo_points",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH points_02 AS (

  SELECT * 
  
  FROM {{ ref('points_02')}}

),

create_geo_points AS (

  {{
    andre_spatial_09.CreatePoint(
      'points_02', 
      [['start_long', 'start_lat', 'start_point'], ['destination_long', 'destination_lat', 'dest_point']]
    )
  }}

)

SELECT *

FROM create_geo_points
