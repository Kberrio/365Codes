import java.util.*;

public class MemoryBlockGame {
    private char[][] board;
    private char[][] hiddenBoard;
    private int size;
    private int pairsLeft;
    private Scanner scanner;

    public MemoryBlockGame(int size) {
        this.size = size;
        this.board = new char[size][size];
        this.hiddenBoard = new char[size][size];
        this.scanner = new Scanner(System.in);
        this.pairsLeft = size * size / 2;
        initializeBoard();
    }

    public void initializeBoard() {
        List<Character> characters = new ArrayList<>();
        for (char ch = 'A'; ch < 'A' + size * size / 2; ch++) {
            characters.add(ch);
            characters.add(ch);
        }
        Collections.shuffle(characters);

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                board[i][j] = '_';
                hiddenBoard[i][j] = characters.remove(0);
            }
        }
    }

    public void displayBoard() {
        System.out.print("  ");
        for (int i = 0; i < size; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        for (int i = 0; i < size; i++) {
            System.out.print(i + " ");
            for (int j = 0; j < size; j++) {
                if (board[i][j] == '_') {
                    System.out.print("_ ");
                } else {
                    System.out.print(board[i][j] + " ");
                }
            }
            System.out.println();
        }
    }

    public boolean isMatched(int row1, int col1, int row2, int col2) {
        return hiddenBoard[row1][col1] == hiddenBoard[row2][col2];
    }

    public void revealBlock(int row, int col) {
        board[row][col] = hiddenBoard[row][col];
    }

    public void play() {
        while (pairsLeft > 0) {
            displayBoard();
            System.out.print("Enter row and column of the first block (separated by space): ");
            int row1 = scanner.nextInt();
            int col1 = scanner.nextInt();
            revealBlock(row1, col1);
            displayBoard();

            System.out.print("Enter row and column of the second block (separated by space): ");
            int row2 = scanner.nextInt();
            int col2 = scanner.nextInt();
            revealBlock(row2, col2);
            displayBoard();

            if (isMatched(row1, col1, row2, col2)) {
                System.out.println("Matched!");
                pairsLeft--;
            } else {
                System.out.println("Not Matched! Try again.");
                board[row1][col1] = '_';
                board[row2][col2] = '_';
            }
        }
        System.out.println("Congratulations! You've matched all pairs.");
    }

    public static void main(String[] args) {
        MemoryBlockGame game = new MemoryBlockGame(4); // Change the size of the board here
        game.play();
    }
}
