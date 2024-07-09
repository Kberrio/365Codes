import java.util.*;

public class PairMatchingGame {
    private static final int BOARD_SIZE = 4;
    private static final String[] SYMBOLS = {"A", "B", "C", "D", "E", "F", "G", "H"};
    private String[][] board;
    private boolean[][] revealed;
    private int pairsFound;

    public PairMatchingGame() {
        board = new String[BOARD_SIZE][BOARD_SIZE];
        revealed = new boolean[BOARD_SIZE][BOARD_SIZE];
        pairsFound = 0;
        initializeBoard();
    }

    private void initializeBoard() {
        List<String> symbolsList = new ArrayList<>(Arrays.asList(SYMBOLS));
        symbolsList.addAll(Arrays.asList(SYMBOLS));
        Collections.shuffle(symbolsList);

        int index = 0;
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                board[i][j] = symbolsList.get(index++);
                revealed[i][j] = false;
            }
        }
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);
        while (pairsFound < BOARD_SIZE * BOARD_SIZE / 2) {
            printBoard();
            System.out.println("Enter the coordinates of two cards (row1 col1 row2 col2):");
            int row1 = scanner.nextInt();
            int col1 = scanner.nextInt();
            int row2 = scanner.nextInt();
            int col2 = scanner.nextInt();

            if (isValidMove(row1, col1, row2, col2)) {
                if (board[row1][col1].equals(board[row2][col2])) {
                    System.out.println("Match found!");
                    revealed[row1][col1] = true;
                    revealed[row2][col2] = true;
                    pairsFound++;
                } else {
                    System.out.println("No match. Try again.");
                    printCard(row1, col1);
                    printCard(row2, col2);
                    System.out.println();
                }
            } else {
                System.out.println("Invalid move. Try again.");
            }
        }
        System.out.println("Congratulations! You've found all pairs!");
    }

    private boolean isValidMove(int row1, int col1, int row2, int col2) {
        return isValidCoordinate(row1, col1) && isValidCoordinate(row2, col2) &&
               !revealed[row1][col1] && !revealed[row2][col2] &&
               !(row1 == row2 && col1 == col2);
    }

    private boolean isValidCoordinate(int row, int col) {
        return row >= 0 && row < BOARD_SIZE && col >= 0 && col < BOARD_SIZE;
    }

    private void printBoard() {
        System.out.print("  ");
        for (int j = 0; j < BOARD_SIZE; j++) {
            System.out.print(j + " ");
        }
        System.out.println();

        for (int i = 0; i < BOARD_SIZE; i++) {
            System.out.print(i + " ");
            for (int j = 0; j < BOARD_SIZE; j++) {
                if (revealed[i][j]) {
                    System.out.print(board[i][j] + " ");
                } else {
                    System.out.print("* ");
                }
            }
            System.out.println();
        }
    }

    private void printCard(int row, int col) {
        System.out.println("Card at (" + row + ", " + col + "): " + board[row][col]);
    }

    public static void main(String[] args) {
        PairMatchingGame game = new PairMatchingGame();
        game.play();
    }
}