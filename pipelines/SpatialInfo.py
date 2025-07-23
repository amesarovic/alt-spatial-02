Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    SpatialInfo__compute_spatial_area = Task(
        task_id = "SpatialInfo__compute_spatial_area", 
        component = "Model", 
        modelName = "SpatialInfo__compute_spatial_area"
    )
