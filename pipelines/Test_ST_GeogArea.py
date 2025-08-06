Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Test_ST_GeogArea__test_geog_area = Task(
        task_id = "Test_ST_GeogArea__test_geog_area", 
        component = "Model", 
        modelName = "Test_ST_GeogArea__test_geog_area"
    )
