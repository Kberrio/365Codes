using System;

class GuessTheNumber
{
    static void Main(string[] args)
    {
        Random random = new Random();
        int numberToGuess = random.Next(1, 101);
        int numberOfGuesses = 0;
        bool hasGuessedCorrectly = false;

        Console.WriteLine("Welcome to 'Guess the Number'!");
        Console.WriteLine("I'm thinking of a number between 1 and 100.");
        Console.WriteLine("Can you guess what it is?");

        while (!hasGuessedCorrectly)
        {
            Console.Write("Enter your guess: ");
            string input = Console.ReadLine();
            int playerGuess;

            if (int.TryParse(input, out playerGuess))
            {
                numberOfGuesses++;

                if (playerGuess > numberToGuess)
                {
                    Console.WriteLine("Too high! Try again.");
                }
                else if (playerGuess < numberToGuess)
                {
                    Console.WriteLine("Too low! Try again.");
                }
                else
                {
                    Console.WriteLine($"Congratulations! You've guessed the number in {numberOfGuesses} guesses.");
                    hasGuessedCorrectly = true;
                }
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a number.");
            }
        }
    }
}
