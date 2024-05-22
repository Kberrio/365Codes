import Foundation

// Function to get a random number between 1 and 100
func getRandomNumber() -> Int {
    return Int(arc4random_uniform(100)) + 1
}

// Function to start the guessing game
func startGuessingGame() {
    let randomNumber = getRandomNumber()
    var userGuess: Int? = nil
    var numberOfGuesses = 0
    
    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Can you guess what it is?")
    
    while userGuess != randomNumber {
        print("Enter your guess: ", terminator: "")
        
        // Read user input and convert to integer
        if let input = readLine(), let guess = Int(input) {
            userGuess = guess
            numberOfGuesses += 1
            
            // Provide feedback to the user
            if userGuess! < randomNumber {
                print("Too low! Try again.")
            } else if userGuess! > randomNumber {
                print("Too high! Try again.")
            } else {
                print("Congratulations! You guessed the correct number in \(numberOfGuesses) tries.")
            }
        } else {
            print("Invalid input. Please enter a number between 1 and 100.")
        }
    }
}

// Start the game
startGuessingGame()
