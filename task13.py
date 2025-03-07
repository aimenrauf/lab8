import heapq
class Process:
    def __init__(self, process_id, name, priority):
        self.process_id = process_id
        self.name = name
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority
    def __str__(self):
        return f"Process(id={self.process_id}, name='{self.name}', priority={self.priority})"
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0  
    def enqueue(self, process):
        heapq.heappush(self.queue, (process.priority, self.counter, process))
        self.counter += 1
        print(f"Added: {process}")
    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[2]
        raise IndexError("dequeue from empty priority queue")
    def is_empty(self):
        return len(self.queue) == 0
    def peek(self):
        if not self.is_empty():
            return self.queue[0][2]
        return None
    def __str__(self):
        return " -> ".join(str(item[2]) for item in self.queue)
process_queue = PriorityQueue()
processes = [
    Process(process_id=1, name="Process A", priority=3),
    Process(process_id=2, name="Process B", priority=1),
    Process(process_id=3, name="Process C", priority=2),
    Process(process_id=4, name="Process D", priority=1),
    Process(process_id=5, name="Process E", priority=5),
    ]
for process in processes:
    process_queue.enqueue(process)
print("\nProcessing the queue...\n")
while not process_queue.is_empty():
    current_process = process_queue.dequeue()
    print(f"Executing: {current_process}")
print("\nRemaining processes in the queue:")
print(process_queue)