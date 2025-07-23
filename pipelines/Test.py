Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_Test_TextToColumns_1 = Task(
        task_id = "model_Test_TextToColumns_1", 
        component = "Model", 
        modelName = "model_Test_TextToColumns_1"
    )
    model_Test_DynamicSelect_1 = Task(
        task_id = "model_Test_DynamicSelect_1", 
        component = "Model", 
        modelName = "model_Test_DynamicSelect_1"
    )
    new_england = Task(
        task_id = "new_england", 
        component = "Dataset", 
        table = {"name" : "new_england", "sourceType" : "Source", "sourceName" : "andre_dev.alteryx_spatial", "alias" : ""}
    )
    model_Test_Limit_1 = Task(task_id = "model_Test_Limit_1", component = "Model", modelName = "model_Test_Limit_1")
    new_england.out >> model_Test_Limit_1.in_0
