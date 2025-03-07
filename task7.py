class Task:
    def __init__(self, task_id, burst_time):
        self.task_id = task_id
        self.burst_time = burst_time
    def __str__(self):
        return f"Task(id={self.task_id}, burst_time={self.burst_time})"
        
class SimpleQueue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

class RoundRobinScheduler:
    def __init__(self, quantum):
        self.task_queue = SimpleQueue()
        self.quantum = quantum  
    def add_task(self, task):
        self.task_queue.enqueue(task)
        print(f"Added {task} to the queue.")
    def schedule_tasks(self):
        while not self.task_queue.is_empty():
            task = self.task_queue.dequeue()
            print(f"Processing {task}...")
            if task.burst_time > self.quantum:
                task.burst_time -= self.quantum
                print(f"Task {task.task_id} did not finish. Remaining burst time: {task.burst_time}.")
                self.task_queue.enqueue(task)
            else:
                print(f"Task {task.task_id} completed.")
                task.burst_time = 0  
def simulate_round_robin():
    scheduler = RoundRobinScheduler(quantum=3) 
    tasks = [
        Task(task_id=1, burst_time=10),
        Task(task_id=2, burst_time=5),
        Task(task_id=3, burst_time=8)
    ]
    for task in tasks:
        scheduler.add_task(task)
    print("\nStarting Round Robin scheduling...\n")
    scheduler.schedule_tasks()

simulate_round_robin()