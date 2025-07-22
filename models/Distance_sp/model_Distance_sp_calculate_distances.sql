{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdf5cvcx__Distance_sp__calculate_distances",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH distances AS (

  SELECT * 
  
  FROM {{ ref('distances')}}

),

calculate_distances AS (

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

FROM calculate_distances
