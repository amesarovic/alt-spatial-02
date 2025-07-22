{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdesd3ws__Buffer_Delta__buffer_new_england",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH new_england AS (

  SELECT * 
  
  FROM {{ source('andre_dev.alteryx_spatial', 'new_england') }}

),

buffer_new_england AS (

  {{
    andre_spatial_09.Buffer(
      'new_england', 
      [{ "name": "name", "dataType": "String" }, { "name": "geometry", "dataType": "String" }], 
      'geometry', 
      25, 
      'miles'
    )
  }}

)

SELECT *

FROM buffer_new_england
