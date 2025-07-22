{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdetnrlp__Distance__calculate_distance",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH distances AS (

  SELECT * 
  
  FROM {{ ref('distances')}}

),

calculate_distance AS (

  {{
    andre_spatial_09.Distance(
      'distances', 
      'pt1', 
      'pt2', 
      'point', 
      'point', 
      true, 
      'kms', 
      true, 
      false, 
      ['pt1', 'pt2']
    )
  }}

)

SELECT *

FROM calculate_distance
