import random

# List of words for the game
word_list = ['python', 'hangman', 'programming', 'code', 'computer', 'keyboard', 'algorithm']

# Choose a word at random from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game variables
display = ['_' for _ in range(word_length)]
lives = 6

print("Welcome to Hangman!")
print(f"The word has {word_length} letters: {' '.join(display)}")

while lives > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed the letter {guess}")
        continue

    if guess in chosen_word:
        print(f"Good guess! {guess} is in the word.")
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print(f"Wrong guess! {guess} is not in the word. You lose a life.")
        lives -= 1
    
    print(f"{' '.join(display)}")
    print(f"Lives left: {lives}")

if '_' not in display:
    print("Congratulations, you won!")
else:
    print("You've run out of lives. Better luck next time!")
    print(f"The word was: {chosen_word}")