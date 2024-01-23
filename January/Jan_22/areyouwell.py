# Initialize a list to store ratings
ratings = []

# Function to get and validate a rating from the user
def get_rating():
    while True:
        try:
            rating = int(input("On a scale from 1 to 10, how are you doing? "))
            if 1 <= rating <= 10:
                return rating
            else:
                print("Invalid rating. Please choose a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

# Ask the user for ratings and store them
num_ratings = int(input("How many ratings do you want to collect? "))
for _ in range(num_ratings):
    rating = get_rating()
    ratings.append(rating)

# Calculate the average rating
if len(ratings) > 0:
    average_rating = sum(ratings) / len(ratings)
    print(f"Average rating based on {len(ratings)} ratings: {average_rating:.2f}")
else:
    print("No ratings collected.")

# You can also store the ratings list or the average_rating in a file or database for future reference.
