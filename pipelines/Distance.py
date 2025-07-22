Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    distances = Task(
        task_id = "distances", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "distances", "sourceType" : "Seed"}
    )
    model_Distance_calc_distance_kms = Task(
        task_id = "model_Distance_calc_distance_kms", 
        component = "Model", 
        modelName = "model_Distance_calc_distance_kms"
    )
    distances.out >> model_Distance_calc_distance_kms.in_0
