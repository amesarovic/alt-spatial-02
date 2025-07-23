Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    points = Task(
        task_id = "points", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points", "sourceType" : "Seed"}
    )
    CreatePoint_sp__create_geo_point = Task(
        task_id = "CreatePoint_sp__create_geo_point", 
        component = "Model", 
        modelName = "CreatePoint_sp__create_geo_point"
    )
    points.out >> CreatePoint_sp__create_geo_point.in_0
