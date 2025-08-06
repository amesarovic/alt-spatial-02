{{
  config({    
    "materialized": "ephemeral",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH Table_1 AS (

  SELECT * 
  
  FROM {{ ref('PolyBuild_output_line')}}

),

buffer_geometry AS (

  {{
    andre_spatial_09.Buffer(
      'Table_1', 
      [
        { "name": "grouping_column_name", "dataType": "String" }, 
        { "name": "geometry_wkt", "dataType": "String" }
      ], 
      'geometry_wkt', 
      300, 
      'meters', 
      'foo'
    )
  }}

)

SELECT *

FROM buffer_geometry
