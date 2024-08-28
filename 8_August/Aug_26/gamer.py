import random

class TextAdventureGame:
    def __init__(self):
        self.player_health = 100
        self.player_gold = 0
        self.enemies = ["Goblin", "Orc", "Troll", "Dragon"]
        self.locations = ["Forest", "Cave", "Castle", "Mountain"]

    def start_game(self):
        print("Welcome to the Text Adventure Game!")
        print("You are a brave adventurer seeking fortune and glory.")
        
        while self.player_health > 0:
            self.take_turn()
        
        print("Game Over! You have been defeated.")
        print(f"You collected {self.player_gold} gold during your adventure.")

    def take_turn(self):
        location = random.choice(self.locations)
        print(f"\nYou find yourself in a {location}.")
        
        choice = input("Do you want to [e]xplore or [r]est? ").lower()
        
        if choice == 'e':
            self.explore()
        elif choice == 'r':
            self.rest()
        else:
            print("Invalid choice. You stumble around and lose 5 health.")
            self.player_health -= 5

    def explore(self):
        if random.random() < 0.7:  # 70% chance of encounter
            enemy = random.choice(self.enemies)
            print(f"You encounter a {enemy}!")
            
            choice = input("Do you want to [f]ight or [r]un? ").lower()
            
            if choice == 'f':
                self.fight(enemy)
            elif choice == 'r':
                self.run()
            else:
                print("Invalid choice. You're caught off guard and lose 10 health.")
                self.player_health -= 10
        else:
            gold_found = random.randint(10, 50)
            self.player_gold += gold_found
            print(f"You found {gold_found} gold!")

    def fight(self, enemy):
        enemy_strength = self.enemies.index(enemy) * 10 + 10
        damage_taken = random.randint(0, enemy_strength)
        self.player_health -= damage_taken
        
        gold_won = random.randint(enemy_strength, enemy_strength * 2)
        self.player_gold += gold_won
        
        print(f"You defeated the {enemy}!")
        print(f"You took {damage_taken} damage and won {gold_won} gold.")
        print(f"Your health: {self.player_health}")

    def run(self):
        escape_chance = random.random()
        if escape_chance > 0.5:
            print("You managed to escape!")
        else:
            damage_taken = random.randint(5, 15)
            self.player_health -= damage_taken
            print(f"You couldn't escape and took {damage_taken} damage while running.")
            print(f"Your health: {self.player_health}")

    def rest(self):
        health_gained = random.randint(5, 15)
        self.player_health = min(100, self.player_health + health_gained)
        print(f"You rest and recover {health_gained} health.")
        print(f"Your health: {self.player_health}")

if __name__ == "__main__":
    game = TextAdventureGame()
    game.start_game()