Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Simplify_02__simplify_geospatial_data = Task(
        task_id = "Simplify_02__simplify_geospatial_data", 
        component = "Model", 
        modelName = "Simplify_02__simplify_geospatial_data"
    )
