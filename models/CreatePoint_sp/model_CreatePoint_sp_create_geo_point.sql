{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdfjqktr__CreatePoint_sp__create_geo_point",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH points AS (

  SELECT * 
  
  FROM {{ ref('points')}}

),

create_geo_point AS (

  {{ andre_spatial_09.CreatePoint('points', [['lon', 'lat', 'point']]) }}

)

SELECT *

FROM create_geo_point
