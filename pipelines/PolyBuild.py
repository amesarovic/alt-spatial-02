Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    poly_build = Task(
        task_id = "poly_build", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "poly_build", "sourceType" : "Seed"}
    )
    model_PolyBuild_build_polyline = Task(
        task_id = "model_PolyBuild_build_polyline", 
        component = "Model", 
        modelName = "model_PolyBuild_build_polyline"
    )
    poly_build.out >> model_PolyBuild_build_polyline.in_0
