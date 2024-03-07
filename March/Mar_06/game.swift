import Foundation

// Function to generate a random number between 1 and 100
func generateRandomNumber() -> Int {
    return Int.random(in: 1...100)
}

// Function to check if the guess is correct
func checkGuess(_ guess: Int, _ target: Int) -> Bool {
    return guess == target
}

// Function to handle the game logic
func playGame() {
    let targetNumber = generateRandomNumber()
    var attempts = 0
    var isCorrect = false
    
    print("Welcome to the Guessing Game!")
    print("Try to guess the number between 1 and 100.")
    
    // Loop until the player guesses the correct number
    repeat {
        print("Enter your guess: ", terminator: "")
        if let input = readLine(), let guess = Int(input) {
            attempts += 1
            if checkGuess(guess, targetNumber) {
                isCorrect = true
            } else {
                if guess < targetNumber {
                    print("Try a higher number!")
                } else {
                    print("Try a lower number!")
                }
            }
        } else {
            print("Invalid input! Please enter a valid number.")
        }
    } while !isCorrect
    
    print("Congratulations! You guessed the number \(targetNumber) in \(attempts) attempts!")
}

// Start the game
playGame()
