import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

class Card {
    private final int value;
    private boolean isFaceUp;

    public Card(int value) {
        this.value = value;
        this.isFaceUp = false;
    }

    public int getValue() {
        return value;
    }

    public boolean isFaceUp() {
        return isFaceUp;
    }

    public void flip() {
        isFaceUp = !isFaceUp;
    }
}

public class MemoryBlocksGame {
    private final List<Card> cards;
    private int numberOfMatches;
    private int numberOfMoves;
    private final Scanner scanner;

    public MemoryBlocksGame(int cardCount) {
        this.cards = new ArrayList<>();
        this.numberOfMatches = 0;
        this.numberOfMoves = 0;
        this.scanner = new Scanner(System.in);

        // Create pairs of cards with values from 1 to cardCount / 2
        for (int i = 1; i <= cardCount / 2; i++) {
            cards.add(new Card(i));
            cards.add(new Card(i));
        }

        // Shuffle the cards
        Collections.shuffle(cards);
    }

    public void play() {
        while (numberOfMatches < cards.size() / 2) {
            displayBoard();
            int choice1 = getValidInput("Enter the first card index: ");
            int choice2 = getValidInput("Enter the second card index: ");

            if (isValidChoice(choice1) && isValidChoice(choice2)) {
                if (cards.get(choice1).getValue() == cards.get(choice2).getValue()) {
                    cards.get(choice1).flip();
                    cards.get(choice2).flip();
                    numberOfMatches++;
                } else {
                    System.out.println("Sorry, no match!");
                }

                cards.get(choice1).flip();
                cards.get(choice2).flip();
                numberOfMoves++;
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        }

        displayBoard();
        System.out.println("Congratulations! You won in " + numberOfMoves + " moves.");
    }

    private void displayBoard() {
        System.out.println("Memory Blocks Game");
        for (int i = 0; i < cards.size(); i++) {
            Card card = cards.get(i);
            if (card.isFaceUp()) {
                System.out.print("[" + card.getValue() + "]");
            } else {
                System.out.print("[ ]");
            }

            if (i % 4 == 3) {
                System.out.println();
            }
        }
        System.out.println();
    }

    private int getValidInput(String prompt) {
        int choice = -1;
        while (choice < 0 || choice >= cards.size()) {
            System.out.print(prompt);
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                choice = -1;
            }
        }
        return choice;
    }

    private boolean isValidChoice(int choice) {
        return choice >= 0 && choice < cards.size() && !cards.get(choice).isFaceUp();
    }

    public static void main(String[] args) {
        int cardCount = 8; // You can change this to set the number of pairs of cards
        MemoryBlocksGame game = new MemoryBlocksGame(cardCount);
        game.play();
    }
}
