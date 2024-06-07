import random

def select_word():
    words = ["perro", "gato", "casa", "sol", "libro", "computadora", "jardín", "agua", "mesa", "pelota"]
    return random.choice(words)

def guess_word():
    guessed_word = False
    attempts = 3
    selected_word = select_word()
    guessed_words = set()
    
    print("Welcome to the Spanish word guessing game!")
    print("You have 3 attempts to guess the word.")
    
    while not guessed_word and attempts > 0:
        print("\nAttempts left:", attempts)
        guess = input("Guess the Spanish word: ").lower()
        
        if guess == selected_word:
            guessed_word = True
            print("Congratulations! You guessed the word correctly:", selected_word)
        elif guess in guessed_words:
            print("You already guessed that word. Try something else.")
        else:
            print("Incorrect guess. Try again.")
            attempts -= 1
            guessed_words.add(guess)
    
    if not guessed_word:
        print("\nSorry, you've run out of attempts.")
        print("The correct word was:", selected_word)

if __name__ == "__main__":
    guess_word()
