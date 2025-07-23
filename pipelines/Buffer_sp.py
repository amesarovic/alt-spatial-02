Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    us_states_lines = Task(
        task_id = "us_states_lines", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "us_states_lines", "sourceType" : "Seed"}
    )
    Buffer_sp__buffer_us_states = Task(
        task_id = "Buffer_sp__buffer_us_states", 
        component = "Model", 
        modelName = "Buffer_sp__buffer_us_states"
    )
    us_states_lines.out >> Buffer_sp__buffer_us_states.in_0
