Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_SpatialMatch_SpatialMatch_0 = Task(
        task_id = "model_SpatialMatch_SpatialMatch_0", 
        component = "Model", 
        modelName = "model_SpatialMatch_SpatialMatch_0"
    )
