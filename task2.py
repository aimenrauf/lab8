class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    def is_empty(self):
        return len(self.items) == 0
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
    def reverse(self):
        stack = Stack()
        while not self.is_empty():
            stack.push(self.dequeue())
        while not stack.is_empty():
            self.enqueue(stack.pop())
    def __str__(self):
        return str(self.items)

q = Queue()
for i in range(1, 6):  
    q.enqueue(i)    
print("Original Queue:")
print(q)  
q.reverse()
print("Reversed Queue:")
print(q) 