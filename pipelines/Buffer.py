Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    us_states_lines = Task(
        task_id = "us_states_lines", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "us_states_lines", "sourceType" : "Seed"}
    )
    Buffer__buffer_us_states = Task(
        task_id = "Buffer__buffer_us_states", 
        component = "Model", 
        modelName = "Buffer__buffer_us_states"
    )
    Table_1 = Task(
        task_id = "Table_1", 
        component = "Dataset", 
        table = {"name" : "PolyBuild_output_line", "sourceType" : "Seed"}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    Buffer__buffer_geometry = Task(
        task_id = "Buffer__buffer_geometry", 
        component = "Model", 
        modelName = "Buffer__buffer_geometry"
    )
    Table_1.out >> Buffer__buffer_geometry.in_0
    us_states_lines.out >> Buffer__buffer_us_states.in_0
