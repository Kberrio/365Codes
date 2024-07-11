python
import random

class Restaurant:
    def __init__(self, name, cuisine, price):
        self.name = name
        self.cuisine = cuisine
        self.price = price

class RestaurantFinder:
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def find_restaurants(self, cuisine=None, max_price=None):
        results = self.restaurants

        if cuisine:
            results = [r for r in results if r.cuisine.lower() == cuisine.lower()]
        
        if max_price:
            results = [r for r in results if r.price <= max_price]

        return results

    def get_random_restaurant(self, cuisine=None, max_price=None):
        matching_restaurants = self.find_restaurants(cuisine, max_price)
        if matching_restaurants:
            return random.choice(matching_restaurants)
        return None

# Usage example
finder = RestaurantFinder()

# Add some sample restaurants
finder.add_restaurant(Restaurant("Pizza Palace", "Italian", 2))
finder.add_restaurant(Restaurant("Burger Bonanza", "American", 1))
finder.add_restaurant(Restaurant("Sushi Sensation", "Japanese", 3))
finder.add_restaurant(Restaurant("Taco Time", "Mexican", 1))
finder.add_restaurant(Restaurant("Pasta Paradise", "Italian", 2))

# Find restaurants
italian_restaurants = finder.find_restaurants(cuisine="Italian")
cheap_restaurants = finder.find_restaurants(max_price=2)

# Get a random restaurant
random_restaurant = finder.get_random_restaurant(cuisine="Italian", max_price=2)

print("Italian Restaurants:", [r.name for r in italian_restaurants])
print("Cheap Restaurants:", [r.name for r in cheap_restaurants])
print("Random Italian Restaurant (max price 2):", random_restaurant.name if random_restaurant else "None found")
