Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    distances = Task(
        task_id = "distances", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "distances", "sourceType" : "Seed"}
    )
    model_Distance_calculate_distance = Task(
        task_id = "model_Distance_calculate_distance", 
        component = "Model", 
        modelName = "model_Distance_calculate_distance"
    )
    distances.out >> model_Distance_calculate_distance.in_0
