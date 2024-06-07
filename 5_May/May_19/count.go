package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	numberToGuess := rand.Intn(100) + 1
	numberOfGuesses := 0
	var playerGuess int

	fmt.Println("Welcome to 'Guess the Number'!")
	fmt.Println("I'm thinking of a number between 1 and 100.")
	fmt.Println("Can you guess what it is?")

	for {
		fmt.Print("Enter your guess: ")
		_, err := fmt.Scan(&playerGuess)
		if err != nil {
			fmt.Println("Invalid input. Please enter a number.")
			continue
		}

		numberOfGuesses++

		if playerGuess > numberToGuess {
			fmt.Println("Too high! Try again.")
		} else if playerGuess < numberToGuess {
			fmt.Println("Too low! Try again.")
		} else {
			fmt.Printf("Congratulations! You've guessed the number in %d guesses.\n", numberOfGuesses)
			break
		}
	}
}
