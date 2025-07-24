Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    poly_build = Task(
        task_id = "poly_build", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "poly_build", "sourceType" : "Seed"}
    )
    PolyBuild_sp__build_polyline = Task(
        task_id = "PolyBuild_sp__build_polyline", 
        component = "Model", 
        modelName = "PolyBuild_sp__build_polyline"
    )
    poly_build.out >> PolyBuild_sp__build_polyline.in_0
