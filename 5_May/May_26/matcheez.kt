import kotlin.random.Random
import kotlin.system.exitProcess

fun main() {
    val boardSize = 4 // 4x4 board
    val board = generateBoard(boardSize)
    val revealed = Array(boardSize) { Array(boardSize) { false } }

    println("Welcome to the Memory Game!")
    printBoard(board, revealed)

    var pairsFound = 0
    val totalPairs = (boardSize * boardSize) / 2

    while (pairsFound < totalPairs) {
        println("Enter the coordinates of the first card (row and column): ")
        val firstCard = readCoordinates(boardSize)
        revealCard(firstCard, board, revealed)

        println("Enter the coordinates of the second card (row and column): ")
        val secondCard = readCoordinates(boardSize)
        revealCard(secondCard, board, revealed)

        printBoard(board, revealed)

        if (board[firstCard.first][firstCard.second] == board[secondCard.first][secondCard.second]) {
            println("You found a match!")
            pairsFound++
        } else {
            println("Not a match.")
            hideCard(firstCard, revealed)
            hideCard(secondCard, revealed)
        }

        printBoard(board, revealed)
    }

    println("Congratulations! You found all pairs!")
}

fun generateBoard(size: Int): Array<Array<Char>> {
    val pairs = (size * size) / 2
    val cards = ('A'..'Z').take(pairs).flatMap { listOf(it, it) }.shuffled(Random(System.currentTimeMillis()))
    val board = Array(size) { Array(size) { ' ' } }
    var index = 0

    for (i in 0 until size) {
        for (j in 0 until size) {
            board[i][j] = cards[index++]
        }
    }

    return board
}

fun printBoard(board: Array<Array<Char>>, revealed: Array<Array<Boolean>>) {
    for (i in board.indices) {
        for (j in board[i].indices) {
            if (revealed[i][j]) {
                print("${board[i][j]} ")
            } else {
                print("* ")
            }
        }
        println()
    }
}

fun readCoordinates(size: Int): Pair<Int, Int> {
    while (true) {
        try {
            val input = readLine()!!.trim().split(" ")
            if (input.size == 2) {
                val row = input[0].toInt()
                val col = input[1].toInt()
                if (row in 0 until size && col in 0 until size) {
                    return Pair(row, col)
                }
            }
            println("Invalid coordinates. Please enter row and column numbers between 0 and ${size - 1}.")
        } catch (e: Exception) {
            println("Invalid input. Please enter numbers.")
        }
    }
}

fun revealCard(coordinates: Pair<Int, Int>, board: Array<Array<Char>>, revealed: Array<Array<Boolean>>) {
    revealed[coordinates.first][coordinates.second] = true
}

fun hideCard(coordinates: Pair<Int, Int>, revealed: Array<Array<Boolean>>) {
    revealed[coordinates.first][coordinates.second] = false
}
