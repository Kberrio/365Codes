import random

# List of activities
activities = [
    "Go for a walk in the park",
    "Read a book for 30 minutes",
    "Try a new recipe for lunch",
    "Watch a movie or TV show",
    "Do a 20-minute workout",
    "Write in your journal",
    "Call a friend or family member",
    "Learn something new online",
    "Visit a local museum or art gallery",
    "Listen to your favorite music",
]

# Function to suggest an activity
def suggest_activity():
    suggestion = random.choice(activities)
    return suggestion

# Main function
def main():
    print("Here's a suggestion for your day:")
    activity = suggest_activity()
    print(activity)

if __name__ == "__main__":
    main()
