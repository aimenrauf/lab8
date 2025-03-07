class ListQueue:
    def __init__(self):
        self.items = []
    def enqueue(self, data):
        self.items.insert(0, data)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.items.pop()
    def peek(self):
        return self.items[-1] if self.items else None
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items) == 0

queue = ListQueue()
queue.enqueue("Hello")
queue.enqueue("World")
print("First item:", queue.peek())  
print("Dequeued:", queue.dequeue())  
print("Queue size:", queue.size())  
