class TaskManager:
    def __init__(self):
        self.tasks = []
    def enqueue(self, data):
        self.tasks.insert(0, data)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.tasks.pop()
    def peek(self):
        return self.tasks[-1] if self.tasks else None
    def size(self):
        return len(self.tasks)
    def is_empty(self):
        return len(self.tasks) == 0
    def display(self):
        return "Queue contents: " + " -> ".join(str(item) for item in self.tasks)

queue = TaskManager()
queue.enqueue("Wash Dishes")
queue.enqueue("COmplete homework")
queue.enqueue("COmplete Manuals")
print(queue.display())  
print("Tasks size:", queue.size())