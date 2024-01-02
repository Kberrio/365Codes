import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    play_game()
