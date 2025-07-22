{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdf41ozt__FindNearest__find_nearest_centers",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH find_nearest_1 AS (

  SELECT * 
  
  FROM {{ ref('find_nearest_1')}}

),

find_nearest_2 AS (

  SELECT * 
  
  FROM {{ ref('find_nearest_2')}}

),

find_nearest_centers AS (

  {{
    andre_spatial_09.FindNearest(
      ['find_nearest_1', 'find_nearest_2'], 
      'customer_point', 
      'center_point', 
      'point', 
      'point', 
      2, 
      1000, 
      'kms', 
      false, 
      ['customer_id', 'customer_point'], 
      ['center_id', 'center_point']
    )
  }}

)

SELECT *

FROM find_nearest_centers
