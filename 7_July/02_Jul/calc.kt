import kotlin.math.pow

class Calculator {
    fun add(a: Double, b: Double) = a + b
    fun subtract(a: Double, b: Double) = a - b
    fun multiply(a: Double, b: Double) = a * b
    fun divide(a: Double, b: Double): Double {
        if (b == 0.0) throw IllegalArgumentException("Cannot divide by zero")
        return a / b
    }
    fun power(base: Double, exponent: Double) = base.pow(exponent)
}

fun main() {
    val calculator = Calculator()
    
    while (true) {
        print("Enter an operation (+, -, *, /, ^) or 'q' to quit: ")
        val operation = readLine()

        if (operation == "q") break

        print("Enter first number: ")
        val a = readLine()?.toDoubleOrNull()
        print("Enter second number: ")
        val b = readLine()?.toDoubleOrNull()

        if (a == null || b == null) {
            println("Invalid input. Please enter valid numbers.")
            continue
        }

        val result = when (operation) {
            "+" -> calculator.add(a, b)
            "-" -> calculator.subtract(a, b)
            "*" -> calculator.multiply(a, b)
            "/" -> try {
                calculator.divide(a, b)
            } catch (e: IllegalArgumentException) {
                println(e.message)
                continue
            }
            "^" -> calculator.power(a, b)
            else -> {
                println("Invalid operation")
                continue
            }
        }

        println("Result: $result")
    }
}