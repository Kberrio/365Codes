import java.util.Scanner;
import java.util.Random;

public class GuessingGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        int secretNumber = random.nextInt(100) + 1; // Generate random number between 1 and 100
        int attempts = 0;
        int guess = 0;
        
        System.out.println("Welcome to the Guessing Game!");
        System.out.println("I have chosen a number between 1 and 100. Try to guess it.");

        while (guess != secretNumber && attempts < 10) { // Limiting the number of attempts to 10
            System.out.print("Enter your guess: ");
            guess = scanner.nextInt();
            attempts++;

            if (guess < secretNumber) {
                System.out.println("Too low! Try again.");
            } else if (guess > secretNumber) {
                System.out.println("Too high! Try again.");
            }
        }

        if (guess == secretNumber) {
            System.out.println("Congratulations! You've guessed the number in " + attempts + " attempts.");
        } else {
            System.out.println("Sorry, you've run out of attempts. The number was: " + secretNumber);
        }
        
        scanner.close();
    }
}
