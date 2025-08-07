Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    simplify_geospatial_data = Task(
        task_id = "simplify_geospatial_data", 
        component = "Simplify_02", 
        relation_name = ["new_england"], 
        _oldMacroProperties = {
          "macroName": "Simplify_02", 
          "projectName": "andre_spatial_09", 
          "parameters": [{"name" : "relation_name", "value" : "['new_england']"},                           {
                            "name": "schema", 
                            "value": "[{"name": "name", "dataType": "String"}, {"name": "geometry", "dataType": "String"}]"
                          },                           {"name" : "destinationColumnNames", "value" : "geometry"},                           {"name" : "threshold", "value" : "1"},                           {"name" : "unit", "value" : "kms"}]
        }, 
        schema = "[{"name": "name", "dataType": "String"}, {"name": "geometry", "dataType": "String"}]", 
        threshold = "1", 
        polygonColumnName = "geometry", 
        unit = "kms"
    )
    new_england = Task(
        task_id = "new_england", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {
          "name": "new_england", 
          "sourceType": "Table", 
          "sourceName": "andre_dev.alteryx_spatial", 
          "alias": "", 
          "additionalProperties": None
        }
    )
    new_england.out >> simplify_geospatial_data.in0
