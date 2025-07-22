Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    points = Task(
        task_id = "points", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points", "sourceType" : "Seed"}
    )
    model_CreatePoint_create_geo_point = Task(
        task_id = "model_CreatePoint_create_geo_point", 
        component = "Model", 
        modelName = "model_CreatePoint_create_geo_point"
    )
    points.out >> model_CreatePoint_create_geo_point.in_0
