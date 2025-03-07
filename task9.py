class ChatMessage:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
    def __str__(self):
        return f"{self.sender}: {self.content}"
class ChatQueue:
    def __init__(self):
        self.messages = []
    def send(self, message):
        self.messages.append(message)
        print(f"Message sent: {message}")
    def receive(self):
        return self.messages

chat_queue = ChatQueue()
chat_queue.send(ChatMessage(sender="Aimen", content="Hello everyone!"))
chat_queue.send(ChatMessage(sender="Sadia", content="Hi Aimen! How are you?"))
chat_queue.send(ChatMessage(sender="Mahnoor", content="Good morning!"))
chat_queue.send(ChatMessage(sender="Aimen", content="I'm doing well, thanks!"))
chat_queue.send(ChatMessage(sender="Sadia", content="What are you all up to today?"))
print("\nChat Messages:")
for msg in chat_queue.receive():
    print(msg)
