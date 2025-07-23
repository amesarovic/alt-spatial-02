{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mdfkja77__Test__DynamicSelect_1",
    "database": "andre_dev",
    "schema": "alteryx_spatial"
  })
}}

WITH DynamicSelect_1 AS (

  {{ DatabricksSqlBasics.DynamicSelect('', '', '', 'SELECT_FIELD_TYPES', "") }}

)

SELECT *

FROM DynamicSelect_1
