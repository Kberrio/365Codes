import random
import math

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

def create_random_tour(cities):
    return random.sample(cities, len(cities))

def tour_length(tour):
    return sum(tour[i].distance(tour[(i+1) % len(tour)]) for i in range(len(tour)))

def mutate(tour):
    i, j = random.sample(range(len(tour)), 2)
    tour[i], tour[j] = tour[j], tour[i]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[start:end]
    child += [city for city in parent2 if city not in child]
    return child

def genetic_algorithm(cities, population_size=100, generations=1000):
    population = [create_random_tour(cities) for _ in range(population_size)]

    for _ in range(generations):
        population = sorted(population, key=tour_length)
        new_population = population[:population_size // 2]

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:population_size // 2], 2)
            child = crossover(parent1, parent2)
            if random.random() < 0.1:  # 10% chance of mutation
                mutate(child)
            new_population.append(child)

        population = new_population

    return min(population, key=tour_length)

# Example usage
cities = [City(random.randint(0, 100), random.randint(0, 100)) for _ in range(20)]
best_tour = genetic_algorithm(cities)
print(f"Best tour length: {tour_length(best_tour)}")