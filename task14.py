class Packet:
    def __init__(self, packet_id, source, destination, data):
        self.packet_id = packet_id
        self.source = source
        self.destination = destination
        self.data = data
    def __str__(self):
        return f"Packet(id={self.packet_id}, from='{self.source}', to='{self.destination}', data='{self.data}')"
class PacketQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, packet):
        self.queue.append(packet)
        print(f"Packet added to queue: {packet}")
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("dequeue from empty packet queue")
    def is_empty(self):
        return len(self.queue) == 0
    def process(self):
        while not self.is_empty():
            packet = self.dequeue()
            print(f"Processing {packet}...")
packet_queue = PacketQueue()
packets = [
    Packet(packet_id=1, source="192.168.1.1", destination="192.168.1.2", data="Hello, World!"),
    Packet(packet_id=2, source="192.168.1.3", destination="192.168.1.4", data="Packet 2 data"),
    Packet(packet_id=3, source="192.168.1.5", destination="192.168.1.6", data="Packet 3 data"),
    Packet(packet_id=4, source="192.168.1.7", destination="192.168.1.8", data="Packet 4 data"),
    ]
for packet in packets:
    packet_queue.enqueue(packet)
print("\nProcessing packets in the queue...\n")
packet_queue.process()