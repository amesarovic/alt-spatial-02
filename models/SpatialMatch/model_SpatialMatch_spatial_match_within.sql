{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdf3os7t__SpatialMatch__spatial_match_within",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH spatial_match_2 AS (

  SELECT * 
  
  FROM {{ ref('spatial_match_2')}}

),

spatial_match_1 AS (

  SELECT * 
  
  FROM {{ ref('spatial_match_1')}}

),

spatial_match_within AS (

  {{
    andre_spatial_09.SpatialMatch(
      ['spatial_match_1', 'spatial_match_2'], 
      [
        ['store_id', 'store_name', 'store_location', 'store_type'], 
        ['zone_id', 'zone_name', 'zone_polygon', 'delivery_fee']
      ], 
      'store_location', 
      'zone_polygon', 
      'within'
    )
  }}

)

SELECT *

FROM spatial_match_within
