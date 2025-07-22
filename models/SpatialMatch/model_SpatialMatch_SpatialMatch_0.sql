{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdf1lmcm__SpatialMatch__SpatialMatch_0",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH SpatialMatch_0 AS (

  {{ andre_spatial_09.SpatialMatch([], [], '', '', '') }}

)

SELECT *

FROM SpatialMatch_0
