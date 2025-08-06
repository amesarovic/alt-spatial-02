{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH new_england AS (

  SELECT * 
  
  FROM {{ source('andre_dev.alteryx_spatial', 'new_england') }}

),

test_geog_area AS (

  {{ andre_spatial_09.Test_ST_GeogArea('points') }}

)

SELECT *

FROM test_geog_area
