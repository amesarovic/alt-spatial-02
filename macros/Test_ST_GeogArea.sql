
{%- macro Test_ST_GeogArea(parameter1) -%}
/*
    select * from {{ parameter1 }}
*/
    select * from {{ parameter1 }}

{%- endmacro -%}
