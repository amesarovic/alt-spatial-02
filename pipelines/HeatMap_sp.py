Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    points = Task(
        task_id = "points", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points", "sourceType" : "Seed"}
    )
    HeatMap_sp__generate_heatmap = Task(
        task_id = "HeatMap_sp__generate_heatmap", 
        component = "Model", 
        modelName = "HeatMap_sp__generate_heatmap"
    )
    points.out >> HeatMap_sp__generate_heatmap.in_0
