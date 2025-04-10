from clearml import PipelineController, Task

# Khởi tạo pipeline controller
pipe = PipelineController(
    name="MLOps Image Pipeline",
    project="MLOps Lab",
    version="1.0"
)

# Tạo Task cho bước preprocess
preprocess_task = Task.create(
    project_name="MLOps Lab",
    task_name="Preprocess",
    script="./src/data_preprocessing.py"
)

pipe.add_step(
    name="preprocess",
    base_task_id=preprocess_task.id,
    execution_queue="default"  # Queue cho bước này
)

# Tạo Task cho bước train + tune
train_task = Task.create(
    project_name="MLOps Lab",
    task_name="Train + Tune",
    script="./src/train.py"
)

pipe.add_step(
    name="train",
    base_task_id=train_task.id,
    parents=["preprocess"],
    execution_queue="default"  # Queue cho bước này
)

# Tạo Task cho bước evaluate
eval_task = Task.create(
    project_name="MLOps Lab",
    task_name="Evaluate",
    script="./src/evaluate.py"
)

pipe.add_step(
    name="evaluate",
    base_task_id=eval_task.id,
    parents=["train"],
    execution_queue="default"  # Queue cho bước này
)

# Bắt đầu chạy pipeline với queue "default"
#pipe.start(queue="default")  # ✅ Thêm queue vào đây
pipe.start_locally()