Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    points_02 = Task(
        task_id = "points_02", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points_02", "sourceType" : "Seed"}
    )
    model_CreatePoint_02_create_geo_points = Task(
        task_id = "model_CreatePoint_02_create_geo_points", 
        component = "Model", 
        modelName = "model_CreatePoint_02_create_geo_points"
    )
    points_02.out >> model_CreatePoint_02_create_geo_points.in_0
