import random
import time
import os

class Ecosystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.entities = {
            'plant': {'symbol': '♣', 'color': '\033[32m', 'growth_rate': 0.1},
            'herbivore': {'symbol': '♘', 'color': '\033[33m', 'reproduction_rate': 0.05, 'death_rate': 0.02},
            'carnivore': {'symbol': '♛', 'color': '\033[31m', 'reproduction_rate': 0.03, 'death_rate': 0.04}
        }

    def initialize(self):
        for _ in range(int(self.width * self.height * 0.3)):
            x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
            entity = random.choice(list(self.entities.keys()))
            self.grid[y][x] = entity

    def update(self):
        new_grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                entity = self.grid[y][x]
                if entity == ' ':
                    if random.random() < self.entities['plant']['growth_rate']:
                        new_grid[y][x] = 'plant'
                elif entity == 'plant':
                    new_grid[y][x] = 'plant'
                    if random.random() < self.entities['herbivore']['reproduction_rate']:
                        self.spawn_nearby(new_grid, x, y, 'herbivore')
                elif entity == 'herbivore':
                    if random.random() < self.entities['herbivore']['death_rate']:
                        continue
                    new_grid[y][x] = 'herbivore'
                    if random.random() < self.entities['carnivore']['reproduction_rate']:
                        self.spawn_nearby(new_grid, x, y, 'carnivore')
                elif entity == 'carnivore':
                    if random.random() < self.entities['carnivore']['death_rate']:
                        continue
                    new_grid[y][x] = 'carnivore'
        self.grid = new_grid

    def spawn_nearby(self, grid, x, y, entity):
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and grid[ny][nx] == ' ':
                grid[ny][nx] = entity
                break

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.grid:
            for cell in row:
                if cell in self.entities:
                    print(f"{self.entities[cell]['color']}{self.entities[cell]['symbol']}\033[0m", end='')
                else:
                    print(' ', end='')
            print()

def run_simulation(width=50, height=25, iterations=100):
    ecosystem = Ecosystem(width, height)
    ecosystem.initialize()
    for _ in range(iterations):
        ecosystem.display()
        ecosystem.update()
        time.sleep(0.1)

if __name__ == "__main__":
    run_simulation()