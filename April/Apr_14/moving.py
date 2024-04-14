import random

class House:
    def __init__(self, address, current_location):
        self.address = address
        self.current_location = current_location

    def move(self, new_location):
        print(f"Moving house at {self.address} from {self.current_location} to {new_location}.")
        self.current_location = new_location

# Function to randomly generate addresses
def generate_address():
    streets = ["Oak", "Maple", "Pine", "Cedar", "Elm"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    return f"{random.choice(streets)} St, {random.choice(cities)}"

# Function to simulate moving houses
def move_houses(houses, new_locations):
    for house, new_location in zip(houses, new_locations):
        house.move(new_location)

# Create some houses
num_houses = 5
houses = [House(generate_address(), "Old Location") for _ in range(num_houses)]

# Generate new locations
new_locations = ["Downtown", "Suburbs", "Rural Area", "Beachfront", "Mountains"]

# Move the houses
move_houses(houses, new_locations)
