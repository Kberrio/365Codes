using System;

namespace GuessTheNumber
{
    class Program
    {
        static void Main(string[] args)
        {
            Random random = new Random();
            int numberToGuess = random.Next(1, 101);
            int numberOfGuesses = 0;
            bool hasGuessedCorrectly = false;

            Console.WriteLine("Welcome to 'Guess the Number'!");
            Console.WriteLine("I'm thinking of a number between 1 and 100. Can you guess what it is?");

            while (!hasGuessedCorrectly)
            {
                Console.Write("Enter your guess: ");
                string input = Console.ReadLine();
                int playerGuess;

                if (int.TryParse(input, out playerGuess))
                {
                    numberOfGuesses++;

                    if (playerGuess == numberToGuess)
                    {
                        hasGuessedCorrectly = true;
                        Console.WriteLine($"Congratulations! You guessed the number in {numberOfGuesses} attempts.");
                    }
                    else if (playerGuess > numberToGuess)
                    {
                        Console.WriteLine("Too high! Try again.");
                    }
                    else
                    {
                        Console.WriteLine("Too low! Try again.");
                    }
                }
                else
                {
                    Console.WriteLine("That's not a valid number. Please enter a number between 1 and 100.");
                }
            }

            Console.WriteLine("Thanks for playing! Press any key to exit.");
            Console.ReadKey();
        }
    }
}
