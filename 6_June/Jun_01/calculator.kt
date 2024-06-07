import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)

    println("Welcome to the Kotlin Calculator")
    println("Please enter the first number:")
    val num1 = scanner.nextDouble()

    println("Please enter an operator (+, -, *, /):")
    val operator = scanner.next()

    println("Please enter the second number:")
    val num2 = scanner.nextDouble()

    val result = when (operator) {
        "+" -> num1 + num2
        "-" -> num1 - num2
        "*" -> num1 * num2
        "/" -> {
            if (num2 != 0.0) {
                num1 / num2
            } else {
                println("Error: Division by zero is not allowed.")
                return
            }
        }
        else -> {
            println("Error: Unknown operator.")
            return
        }
    }

    println("The result of $num1 $operator $num2 is $result")
}
