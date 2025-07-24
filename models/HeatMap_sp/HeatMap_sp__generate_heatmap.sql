{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH points AS (

  SELECT * 
  
  FROM {{ ref('points')}}

),

generate_heatmap AS (

  {{ andre_spatial_09.HeatMap('points', 'lon', 'lat', 8, 10, '', 'constant') }}

)

SELECT *

FROM generate_heatmap
