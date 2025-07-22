Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    find_nearest_1 = Task(
        task_id = "find_nearest_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "find_nearest_1", "sourceType" : "Seed"}
    )
    find_nearest_2 = Task(
        task_id = "find_nearest_2", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "find_nearest_2", "sourceType" : "Seed"}
    )
    model_FindNearest_find_nearest_centers = Task(
        task_id = "model_FindNearest_find_nearest_centers", 
        component = "Model", 
        modelName = "model_FindNearest_find_nearest_centers"
    )
    find_nearest_1.out >> model_FindNearest_find_nearest_centers.in_0
    find_nearest_2.out >> model_FindNearest_find_nearest_centers.in_1
