import time
import random
import threading
class PrintJob:
    def __init__(self, job_id, pages):
        self.job_id = job_id
        self.pages = pages
    def __str__(self):
        return f"PrintJob(id={self.job_id}, pages={self.pages})"
class Queue:
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
    def display(self):
        if self.is_empty():
            return "Queue is empty."
        return "Queue contents: " + " -> ".join(str(item) for item in self.items)
class PrintQueue:
    def __init__(self):
        self.queue = Queue()
    def add_job(self, job):
        self.queue.enqueue(job)
        print(f"Added {job} to the print queue.")
    def process_jobs(self):
        while not self.queue.is_empty():
            job = self.queue.dequeue()
            print(f"Processing {job}...")
            time.sleep(job.pages * 0.5) 
            print(f"Completed {job}.")

def simulate_print_jobs():
    print_queue = PrintQueue()
    for i in range(5):
        pages = random.randint(1, 10) 
        job = PrintJob(job_id=i + 1, pages=pages)
        print_queue.add_job(job)
    print_queue.process_jobs()

simulate_print_jobs()