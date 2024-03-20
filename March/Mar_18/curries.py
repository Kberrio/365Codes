def recommend_curry(protein):
    curry_recipes = {
        'chicken': {
            'name': 'Chicken Curry',
            'ingredients': ['chicken', 'onions', 'tomatoes', 'garlic', 'ginger', 'curry powder', 'coconut milk']
        },
        'beef': {
            'name': 'Beef Rendang',
            'ingredients': ['beef', 'lemongrass', 'coconut milk', 'turmeric', 'ginger', 'chili peppers']
        },
        'lentil': {
            'name': 'Lentil Dahl',
            'ingredients': ['lentils', 'onions', 'tomatoes', 'garlic', 'cumin', 'mustard seeds', 'turmeric']
        },
        'tofu': {
            'name': 'Tofu Thai Green Curry',
            'ingredients': ['tofu', 'green curry paste', 'coconut milk', 'bamboo shoots', 'basil', 'bell pepper']
        }
    }

    recipe = curry_recipes.get(protein.lower())
    if recipe:
        print(f"Suggested Recipe: {recipe['name']}")
        print("Ingredients needed:")
        for ingredient in recipe['ingredients']:
            print(f"- {ingredient}")
    else:
        print("Sorry, we don't have a recipe for that protein. Try chicken, beef, lentil, or tofu.")

# Example usage:
protein = input("Enter the type of protein you want to use (chicken, beef, lentil, tofu): ")
recommend_curry(protein)