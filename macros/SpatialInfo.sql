{%- macro SpatialInfo(table_name, schema, geom_column_name, area, centroid) -%}
  {{ log("table_name=" ~ table_name, info=True) }}
  {{ log("schema=" ~ schema, info=True) }}
  {{ log("geom_column_name=" ~ geom_column_name, info=True) }}
  {{ log("area=" ~ area, info=True) }}
  {{ log("centroid=" ~ centroid, info=True) }}

  SELECT
    ST_AsText(ST_Centroid(ST_GeomFromText({{geom_column_name}}))) as centroid,
    {{geom_column_name}} as input
  FROM
    {{table_name}}
  
{%- endmacro -%}
