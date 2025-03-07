class Message:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
    def __str__(self):
        return f"From: {self.sender}, To: {self.recipient}, Message: '{self.content}'"
class MessageQueue:
    def __init__(self):
        self.messages = []

    def send(self, message):
        self.messages.append(message)
        print(f"Message sent: {message}")

    def receive(self, recipient):
        received_messages = [msg for msg in self.messages if msg.recipient == recipient]
        self.messages = [msg for msg in self.messages if msg.recipient != recipient]  
        return received_messages

m = MessageQueue()
m.send(Message(sender="Aimen", recipient="Sadia", content="Hello Saia!"))
m.send(Message(sender="Sadia", recipient="Mahnoor", content="Hi Mahnoor!"))
m.send(Message(sender="Mahnoor", recipient="Aimen", content="Hi Aimen!"))
m.send(Message(sender="Haseeb", recipient="Sadia", content="Hey Sadia!"))
print("\nMessages for Sadia:")
for msg in m.receive("Sadia"):
    print(msg)
print("\nMessages for Aimen:")
for msg in m.receive("Aimen"):
    print(msg)
print("\nMessages for Mahnoor:")
for msg in m.receive("Mahnoor"):
    print(msg)