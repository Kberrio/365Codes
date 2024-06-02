import java.util.*
import kotlin.math.*

fun main() {
    val scanner = Scanner(System.`in`)

    println("Welcome to the Advanced Kotlin Calculator")

    while (true) {
        println("Please enter an expression to calculate (or type 'exit' to quit):")
        val input = scanner.nextLine()

        if (input.lowercase() == "exit") {
            println("Goodbye!")
            break
        }

        try {
            val result = evaluateExpression(input)
            println("The result is: $result")
        } catch (e: Exception) {
            println("Error: ${e.message}")
        }
    }
}

fun evaluateExpression(expression: String): Double {
    val tokens = tokenize(expression)
    val postfix = infixToPostfix(tokens)
    return evaluatePostfix(postfix)
}

fun tokenize(expression: String): List<String> {
    val regex = Regex("([0-9]+\\.?[0-9]*)|([+\\-*/^%()])|([a-zA-Z]+)")
    return regex.findAll(expression).map { it.value }.toList()
}

fun infixToPostfix(tokens: List<String>): List<String> {
    val precedence = mapOf(
        "+" to 1, "-" to 1, "*" to 2, "/" to 2, "%" to 2, "^ to 3
    )
    val stack = Stack<String>()
    val output = mutableListOf<String>()

    for (token in tokens) {
        when {
            token.toDoubleOrNull() != null -> output.add(token)
            token.matches(Regex("[a-zA-Z]+")) -> stack.push(token)
            token == "(" -> stack.push(token)
            token == ")" -> {
                while (stack.isNotEmpty() && stack.peek() != "(") {
                    output.add(stack.pop())
                }
                if (stack.isNotEmpty() && stack.peek() == "(") {
                    stack.pop()
                }
            }
            else -> {
                while (stack.isNotEmpty() && precedence[token]!! <= precedence[stack.peek()]!!) {
                    output.add(stack.pop())
                }
                stack.push(token)
            }
        }
    }

    while (stack.isNotEmpty()) {
        output.add(stack.pop())
    }

    return output
}

fun evaluatePostfix(postfix: List<String>): Double {
    val stack = Stack<Double>()

    for (token in postfix) {
        when {
            token.toDoubleOrNull() != null -> stack.push(token.toDouble())
            token.matches(Regex("[a-zA-Z]+")) -> {
                val value = stack.pop()
                stack.push(applyFunction(token, value))
            }
            else -> {
                val b = stack.pop()
                val a = stack.pop()
                stack.push(applyOperator(token, a, b))
            }
        }
    }

    return stack.pop()
}

fun applyOperator(operator: String, a: Double, b: Double): Double {
    return when (operator) {
        "+" -> a + b
        "-" -> a - b
        "*" -> a * b
        "/" -> a / b
        "%" -> a % b
        "^" -> a.pow(b)
        else -> throw IllegalArgumentException("Unknown operator: $operator")
    }
}

fun applyFunction(function: String, value: Double): Double {
    return when (function.lowercase()) {
        "sin" -> sin(value)
        "cos" -> cos(value)
        "tan" -> tan(value)
        "sqrt" -> sqrt(value)
        "log" -> log10(value)
        "ln" -> ln(value)
        else -> throw IllegalArgumentException("Unknown function: $function")
    }
}
