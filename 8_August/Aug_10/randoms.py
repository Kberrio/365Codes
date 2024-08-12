import random

class Champion:
    def __init__(self, name, health, attack, ability_power):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.ability_power = ability_power

    def basic_attack(self, target):
        damage = self.attack
        target.health -= damage
        print(f"{self.name} deals {damage} damage to {target.name}!")

    def ability(self, target):
        damage = self.ability_power * 1.5
        target.health -= damage
        print(f"{self.name} uses their ability, dealing {damage} damage to {target.name}!")

champions = [
    Champion("Garen", 200, 20, 10),
    Champion("Lux", 150, 15, 25),
    Champion("Darius", 180, 25, 15),
    Champion("Ahri", 160, 18, 22)
]

def select_champion():
    print("Select your champion:")
    for i, champ in enumerate(champions):
        print(f"{i+1}. {champ.name}")
    while True:
        try:
            choice = int(input("Enter the number of your chosen champion: ")) - 1
            if 0 <= choice < len(champions):
                return champions[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def battle(player, enemy):
    print(f"\nBattle begins! {player.name} vs {enemy.name}")
    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name}: {player.health}/{player.max_health} HP")
        print(f"{enemy.name}: {enemy.health}/{enemy.max_health} HP")
        
        action = input("Choose your action (1 for basic attack, 2 for ability): ")
        if action == "1":
            player.basic_attack(enemy)
        elif action == "2":
            player.ability(enemy)
        else:
            print("Invalid action. Skipping turn.")
        
        if enemy.health <= 0:
            print(f"\nVictory! You defeated {enemy.name}!")
            return
        
        if random.choice([True, False]):
            enemy.basic_attack(player)
        else:
            enemy.ability(player)
        
        if player.health <= 0:
            print(f"\nDefeat! {enemy.name} has defeated you.")
            return

def main():
    print("Welcome to the League of Legends Text Game!")
    player_champion = select_champion()
    enemy_champion = random.choice([c for c in champions if c != player_champion])
    battle(player_champion, enemy_champion)

if __name__ == "__main__":
    main()