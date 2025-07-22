{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdf1tudm__HeatMap__create_heatmap",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH points AS (

  SELECT * 
  
  FROM {{ ref('points')}}

),

create_heatmap AS (

  {{ andre_spatial_09.HeatMap('points', 'lon', 'lat', 8, 10, '', 'constant') }}

)

SELECT *

FROM create_heatmap
