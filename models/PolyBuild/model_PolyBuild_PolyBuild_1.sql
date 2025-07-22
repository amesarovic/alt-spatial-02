{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdevjx6d__PolyBuild__PolyBuild_1",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH us_states_lines AS (

  SELECT * 
  
  FROM {{ ref('us_states_lines')}}

),

PolyBuild_1 AS (

  {{ andre_spatial_09.PolyBuild('us_states_lines', 'SequencePolygon', '', '', '', '') }}

)

SELECT *

FROM PolyBuild_1
