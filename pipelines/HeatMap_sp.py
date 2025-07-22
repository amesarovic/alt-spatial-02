Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    points = Task(
        task_id = "points", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points", "sourceType" : "Seed"}
    )
    model_HeatMap_sp_generate_heatmap = Task(
        task_id = "model_HeatMap_sp_generate_heatmap", 
        component = "Model", 
        modelName = "model_HeatMap_sp_generate_heatmap"
    )
    points.out >> model_HeatMap_sp_generate_heatmap.in_0
