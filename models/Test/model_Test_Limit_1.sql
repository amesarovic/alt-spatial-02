{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdes29i7__Test__Limit_1",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH new_england AS (

  SELECT * 
  
  FROM {{ source('andre_dev.alteryx_spatial', 'new_england') }}

),

Limit_1 AS (

  SELECT * 
  
  FROM new_england AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
