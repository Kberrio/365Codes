import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def display_status(self):
        print(f"Player: {self.name}")
        print(f"Health: {self.health}")
        print("Inventory:", self.inventory)


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0


def battle(player, enemy):
    print("A wild", enemy.name, "appears!")
    while player.health > 0 and enemy.is_alive():
        print("\n1. Attack")
        print("2. Use Item")
        choice = input("Choose your action: ")
        if choice == "1":
            print("You attack the", enemy.name)
            enemy.take_damage(20)
            time.sleep(1)
            print(f"The {enemy.name}'s health is now {enemy.health}")
            if enemy.is_alive():
                print(f"The {enemy.name} attacks you!")
                player.take_damage(enemy.damage)
                print(f"Your health is now {player.health}")
        elif choice == "2":
            print("You don't have any items...")

    if player.health <= 0:
        print("You have been defeated!")
    else:
        print("You defeated the", enemy.name, "and gained 50 gold!")
        player.add_to_inventory("Gold")


def main():
    print("Welcome to the Adventure Game!")
    player_name = input("Enter your name: ")
    player = Player(player_name)

    print("\nYou are walking through a dark forest...")
    time.sleep(2)

    print("\nYou encounter a scary monster!")
    time.sleep(1)
    enemy = Enemy("Monster", 50, 10)

    battle(player, enemy)

    print("\nYou continue your journey...")
    time.sleep(1)
    print("More adventures await!")


if __name__ == "__main__":
    main()
