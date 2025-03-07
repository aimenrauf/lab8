class Call:
    def __init__(self, call_id, customer_name):
        self.call_id = call_id
        self.customer_name = customer_name
    def __str__(self):
        return f"Call(id={self.call_id}, customer='{self.customer_name}')"
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
class CallCenter:
    def __init__(self):
        self.call_queue = SimpleQueue()
    def receive_call(self, call):
        self.call_queue.enqueue(call)
        print(f"Received {call}.")
    def answer_calls(self):
        while not self.call_queue.is_empty():
            call = self.call_queue.dequeue()
            print(f"Answering {call}...")
            time_to_handle = 1  
            print(f"Handling {call} for {time_to_handle} second(s)...")
            time.sleep(time_to_handle)
            print(f"Completed {call}.")
def simulate_call_center():
    call_center = CallCenter()
    for i in range(3):
        customer_name = f"Customer {i + 1}"
        call = Call(call_id=i + 1, customer_name=customer_name)
        call_center.receive_call(call)
    print("\nStarting to answer calls...\n")
    call_center.answer_calls()


import time  
simulate_call_center()