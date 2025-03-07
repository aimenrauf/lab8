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

def is_palindrome(s):
    queue = Queue()
    for char in s:
        queue.enqueue(char)
    for i in range(queue.size() // 2):
        front_char = queue.dequeue()
        temp_stack = []
        while not queue.is_empty():
            temp_stack.append(queue.dequeue())
        if front_char != temp_stack.pop():
            return False
        for char in temp_stack:
            queue.enqueue(char)
    return True

test_strings = ["racecar", "hello", "level", "world", "madam"]    
for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' is a palindrome: {result}")