{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdfkja77__Test__TextToColumns_1",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH TextToColumns_1 AS (

  {{
    DatabricksSqlBasics.TextToColumns(
      '', 
      '', 
      "", 
      '', 
      1, 
      'Leave extra in last column', 
      'root', 
      'generated', 
      'generated_column'
    )
  }}

)

SELECT *

FROM TextToColumns_1
