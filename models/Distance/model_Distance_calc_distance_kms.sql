{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdezq40d__Distance__calc_distance_kms",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH distances AS (

  SELECT * 
  
  FROM {{ ref('distances')}}

),

calc_distance_kms AS (

  {{
    andre_spatial_09.Distance(
      'distances', 
      'source_point', 
      'dest_point', 
      'point', 
      'point', 
      true, 
      'kms', 
      true, 
      true, 
      ['start_city', 'destination_city', 'source_point', 'dest_point']
    )
  }}

)

SELECT *

FROM calc_distance_kms
