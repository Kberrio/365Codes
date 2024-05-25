fun isLeapYear(year: Int): Boolean {
    return when {
        year % 400 == 0 -> true
        year % 100 == 0 -> false
        year % 4 == 0 -> true
        else -> false
    }
}

fun main() {
    val year = 2024
    if (isLeapYear(year)) {
        println("$year is a leap year.")
    } else {
        println("$year is not a leap year.")
    }
}
