Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    spatial_match_1 = Task(
        task_id = "spatial_match_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "spatial_match_1", "sourceType" : "Seed"}
    )
    spatial_match_2 = Task(
        task_id = "spatial_match_2", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "spatial_match_2", "sourceType" : "Seed"}
    )
    model_SpatialMatch_sp_spatial_match_within = Task(
        task_id = "model_SpatialMatch_sp_spatial_match_within", 
        component = "Model", 
        modelName = "model_SpatialMatch_sp_spatial_match_within"
    )
    spatial_match_1.out >> model_SpatialMatch_sp_spatial_match_within.in_0
    spatial_match_2.out >> model_SpatialMatch_sp_spatial_match_within.in_1
