Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    points = Task(
        task_id = "points", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points", "sourceType" : "Seed"}
    )
    model_HeatMap_create_heatmap = Task(
        task_id = "model_HeatMap_create_heatmap", 
        component = "Model", 
        modelName = "model_HeatMap_create_heatmap"
    )
    points.out >> model_HeatMap_create_heatmap.in_0
