Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    us_states_lines = Task(
        task_id = "us_states_lines", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "us_states_lines", "sourceType" : "Seed"}
    )
    model_PolyBuild_PolyBuild_1 = Task(
        task_id = "model_PolyBuild_PolyBuild_1", 
        component = "Model", 
        modelName = "model_PolyBuild_PolyBuild_1"
    )
    us_states_lines.out >> model_PolyBuild_PolyBuild_1.in_0
