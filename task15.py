class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
    def __str__(self):
        return f"Task(id={self.task_id}, description='{self.description}')"
class GPU:
    def __init__(self, gpu_id):
        self.gpu_id = gpu_id
        self.is_available = True
    def process_task(self, task):
        if self.is_available:
            self.is_available = False
            print(f"GPU {self.gpu_id} is processing {task}...")
            self.is_available = True
            print(f"GPU {self.gpu_id} has completed {task}.")
        else:
            print(f"GPU {self.gpu_id} is currently busy.")
class TaskQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, task):
        self.queue.append(task)
        print(f"Task added to queue: {task}")
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  
        raise IndexError("dequeue from empty task queue")
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0
    def process_tasks(self, gpus):
        while not self.is_empty():
            task = self.dequeue()
            for gpu in gpus:
                if gpu.is_available:
                    gpu.process_task(task)
                    break
            else:
                print("No available GPUs to process the task. Task will be re-enqueued.")
                self.enqueue(task)  
task_queue = TaskQueue()
tasks = [
    Task(task_id=1, description="Train model A"),
    Task(task_id=2, description="Evaluate model B"),
    Task(task_id=3, description="Fine-tune model C"),
    Task(task_id=4, description="Run inference on model D"),
    ]
for task in tasks:
    task_queue.enqueue(task)
gpus = [GPU(gpu_id=1), GPU(gpu_id=2)] 
print("\nProcessing tasks in the queue...\n")
task_queue.process_tasks(gpus)