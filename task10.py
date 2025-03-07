class Passenger:
    def __init__(self, passenger_id, name):
        self.passenger_id = passenger_id
        self.name = name
    def __str__(self):
        return f"Passenger(id={self.passenger_id}, name='{self.name}')"
class Ride:
    def __init__(self, ride_id):
        self.ride_id = ride_id
        self.passengers = []
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    def __str__(self):
        passenger_names = ', '.join([p.name for p in self.passengers])
        return f"Ride(id={self.ride_id}, passengers=[{passenger_names}])"
class RideSharingQueue:
    def __init__(self):
        self.passenger_queue = []
    def add_passenger(self, passenger):
        self.passenger_queue.append(passenger)
        print(f"Added {passenger} to the queue.")
    def assign_ride(self, ride_id, max_passengers):
        ride = Ride(ride_id)
        while self.passenger_queue and len(ride.passengers) < max_passengers:
            passenger = self.passenger_queue.pop(0) 
            ride.add_passenger(passenger)
        return ride

ride_sharing_queue = RideSharingQueue()
passengers = [
    Passenger(passenger_id=1, name="Alice"),
    Passenger(passenger_id=2, name="Bob"),
    Passenger(passenger_id=3, name="Charlie"),
    Passenger(passenger_id=4, name="David"),
    Passenger(passenger_id=5, name="Eve"),
    ]

for passenger in passengers:
    ride_sharing_queue.add_passenger(passenger)
print("\nAssigning rides...\n")
ride1 = ride_sharing_queue.assign_ride(ride_id=101, max_passengers=3)
print(ride1)
ride2 = ride_sharing_queue.assign_ride(ride_id=102, max_passengers=3)
print(ride2)