{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdfekda2__Generalize_sp__generalize_us_states",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH us_states_lines AS (

  SELECT * 
  
  FROM {{ ref('us_states_lines')}}

),

generalize_us_states AS (

  {{
    andre_spatial_09.Generalize(
      'us_states_lines', 
      [{ "name": "name", "dataType": "String" }, { "name": "geometry", "dataType": "String" }], 
      'geometry', 
      20, 
      'miles'
    )
  }}

)

SELECT *

FROM generalize_us_states
