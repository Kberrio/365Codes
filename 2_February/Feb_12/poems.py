import random

# Define lists of phrases for each part of the poem
line1_options = ["In the quiet of the night,", "Underneath the moonlit sky,", "Amidst the whispers of the wind,"]
line2_options = ["A solitary figure wanders,", "Dreams dance like fireflies,", "Echoes of memories linger,"]
line3_options = ["Searching for meaning in shadows.", "Yearning for a touch of grace.", "Lost in the labyrinth of time."]

# Function to generate a random poem
def generate_poem():
    # Randomly select a phrase from each list
    line1 = random.choice(line1_options)
    line2 = random.choice(line2_options)
    line3 = random.choice(line3_options)
    
    # Combine the lines to form the poem
    poem = line1 + "\n" + line2 + "\n" + line3
    
    return poem

# Generate and print a random poem
print("Here's your random poem:")
print(generate_poem())
