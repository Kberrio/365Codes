import kotlinx.coroutines.*
import kotlin.reflect.KProperty

// Inline class
@JvmInline
value class Percentage(val value: Int)

// Sealed interface
sealed interface Shape {
    fun area(): Double
}

// Data class implementing sealed interface
data class Circle(val radius: Double) : Shape {
    override fun area() = Math.PI * radius * radius
}

// Object declaration implementing sealed interface
object EmptyShape : Shape {
    override fun area() = 0.0
}

// Extension function
fun Shape.perimeter(): Double = when (this) {
    is Circle -> 2 * Math.PI * radius
    is EmptyShape -> 0.0
}

// Higher-order function with function type
fun <T> measureTime(action: () -> T): Pair<T, Long> {
    val startTime = System.nanoTime()
    val result = action()
    val endTime = System.nanoTime()
    return result to (endTime - startTime)
}

// Custom delegate
class Memoize<T, R>(private val func: (T) -> R) {
    private val cache = mutableMapOf<T, R>()
    operator fun getValue(thisRef: Any?, property: KProperty<*>) = { arg: T ->
        cache.getOrPut(arg) { func(arg) }
    }
}

// Coroutine
suspend fun fetchData(): String {
    delay(1000) // Simulating network delay
    return "Data fetched"
}

// Main function using coroutines
suspend fun main() = coroutineScope {
    val fibonacci: (Int) -> Long by Memoize { n ->
        if (n <= 1) n.toLong() else fibonacci(n - 1) + fibonacci(n - 2)
    }

    val job = launch {
        val (result, time) = measureTime { fibonacci(40) }
        println("Fibonacci(40) = $result, calculated in ${time / 1_000_000} ms")
    }

    val deferred = async { fetchData() }
    
    val shape: Shape = Circle(5.0)
    println("Area of $shape: ${shape.area()}")
    println("Perimeter of $shape: ${shape.perimeter()}")

    val percentage = Percentage(75)
    println("Percentage: ${percentage.value}%")

    job.join()
    println(deferred.await())
}