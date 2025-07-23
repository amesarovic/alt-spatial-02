{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH us_states_lines AS (

  SELECT * 
  
  FROM {{ ref('us_states_lines')}}

),

buffer_us_states AS (

  {{
    andre_spatial_09.Buffer(
      'us_states_lines', 
      [{ "name": "name", "dataType": "String" }, { "name": "geometry", "dataType": "String" }], 
      'geometry', 
      25, 
      'miles'
    )
  }}

)

SELECT *

FROM buffer_us_states
