class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    def __str__(self):
        return f"{self.title} by {self.artist}"
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    def enqueue(self, song):
        if self.size == self.capacity:
            print("Queue is full. Cannot add more songs.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = song
        self.size += 1
        print(f"Added: {song}")
    def dequeue(self):
        if self.size == 0:
            print("Queue is empty. No songs to play.")
            return None
        song = self.queue[self.front]
        self.queue[self.front] = None 
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return song
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.capacity
    def current_song(self):
        if self.is_empty():
            return None
        return self.queue[self.front]
    def __str__(self):
        songs = []
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            songs.append(str(self.queue[index]))
        return " -> ".join(songs)

playlist = CircularQueue(capacity=5)
songs = [
    Song("Song 1", "Artist Aimen"),
    Song("Song 2", "Artist Sadia"),
    Song("Song 3", "Artist Mahnoor"),
    Song("Song 4", "Artist Haseeb"),
    Song("Song 5", "Artist Sania"),
    Song("Song 6", "Artist Hira"),  
    ]
for song in songs:
    playlist.enqueue(song)
print("\nPlaying songs in the playlist:")
for _ in range(7):  
    current = playlist.current_song()
    if current:
        print(f"Now playing: {current}")
        playlist.dequeue()  
    else:
        print("No more songs to play.")
print("\nRemaining songs in the playlist:")
print(playlist)