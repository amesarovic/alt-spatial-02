Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    SpatialInfo_02__compute_spatial_info = Task(
        task_id = "SpatialInfo_02__compute_spatial_info", 
        component = "Model", 
        modelName = "SpatialInfo_02__compute_spatial_info"
    )
