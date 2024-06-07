import random

class Room:
    def __init__(self, name, description, connections):
        self.name = name
        self.description = description
        self.connections = connections

    def __str__(self):
        return f"{self.name}\n{self.description}\n"

class Player:
    def __init__(self):
        self.current_room = None
        self.items = []

    def move(self, direction):
        if direction in self.current_room.connections:
            self.current_room = self.current_room.connections[direction]
            print(f"You are now in the {self.current_room.name}.")
            print(self.current_room)
        else:
            print("You can't go that way!")

    def check_inventory(self):
        if self.items:
            print("You are carrying:")
            for item in self.items:
                print(item)
        else:
            print("You are not carrying anything.")

class Game:
    def __init__(self):
        self.player = Player()
        self.create_rooms()
        self.intro_text = "Welcome to the Text Adventure Game! Type 'quit' at any time to exit."

    def create_rooms(self):
        self.room1 = Room("Room 1", "This is the starting room.", {"east": None})
        self.room2 = Room("Room 2", "This room has a key.", {"west": self.room1, "east": None})
        self.room3 = Room("Room 3", "This room has a locked door.", {"west": self.room2})
        self.room4 = Room("Room 4", "This room has a treasure chest.", {"west": self.room3})
        self.room5 = Room("Room 5", "This room is empty.", {"south": self.room4})

        # Add items to rooms
        self.room2.items = ["key"]
        self.room4.items = ["treasure chest"]

        # Set starting room
        self.player.current_room = self.room1

    def start(self):
        print(self.intro_text)
        print(self.player.current_room)
        self.game_loop()

    def game_loop(self):
        while True:
            command = input("> ").lower()

            if command == 'quit':
                print("Thanks for playing!")
                break
            elif command == 'inventory':
                self.player.check_inventory()
            elif command in ['north', 'south', 'east', 'west']:
                self.player.move(command)
            else:
                print("Invalid command. Type 'north', 'south', 'east', 'west', 'inventory', or 'quit'.")

game = Game()
game.start()
