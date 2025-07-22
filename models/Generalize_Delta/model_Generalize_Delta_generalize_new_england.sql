{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdet1ck6__Generalize_Delta__generalize_new_england",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH new_england AS (

  SELECT * 
  
  FROM {{ source('andre_dev.alteryx_spatial', 'new_england') }}

),

generalize_new_england AS (

  {{
    andre_spatial_09.Generalize(
      'new_england', 
      [{ "name": "name", "dataType": "String" }, { "name": "geometry", "dataType": "String" }], 
      'geometry', 
      25, 
      'kms'
    )
  }}

)

SELECT *

FROM generalize_new_england
