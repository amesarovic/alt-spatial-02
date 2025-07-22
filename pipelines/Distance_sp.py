Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    distances = Task(
        task_id = "distances", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "distances", "sourceType" : "Seed"}
    )
    model_Distance_sp_calculate_distances = Task(
        task_id = "model_Distance_sp_calculate_distances", 
        component = "Model", 
        modelName = "model_Distance_sp_calculate_distances"
    )
    distances.out >> model_Distance_sp_calculate_distances.in_0
