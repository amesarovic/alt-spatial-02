{%- macro SpatialInfo(table_name, schema, geom_column_name, area) -%}
  {{ log("table_name=" ~ table_name, info=True) }}
  {{ log("schema=" ~ schema, info=True) }}
  {{ log("geom_column_name=" ~ geom_column_name, info=True) }}
  {{ log("area=" ~ arexa, info=True) }}

  SELECT
    ST_AsText(ST_Centroid(ST_GeomFromText({{geom_column_name}}))) as centroid,
    round(ST_GeogArea({{geom_column_name}})/1000000) as area_kms,
    round(ST_GeogArea({{geom_column_name}})/1000000/2.59) as area_miles,
    {{geom_column_name}} as input
  FROM
    {{table_name}}
  
{%- endmacro -%}
