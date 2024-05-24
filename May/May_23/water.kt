import java.util.Scanner

fun main() {
    val dailyGoal = 2000 // daily goal in milliliters
    var totalIntake = 0
    val scanner = Scanner(System.`in`)

    println("Welcome to the Water Tracker!")
    println("Your daily goal is $dailyGoal ml.")
    
    while (true) {
        println("Enter the amount of water you drank in ml (or type 'done' to finish):")
        val input = scanner.nextLine()

        if (input.toLowerCase() == "done") {
            break
        }

        try {
            val intake = input.toInt()
            totalIntake += intake
            println("You have added $intake ml. Total intake so far: $totalIntake ml.")
        } catch (e: NumberFormatException) {
            println("Invalid input. Please enter a number or type 'done'.")
        }
    }

    println("End of the day summary:")
    println("You drank a total of $totalIntake ml today.")
    
    if (totalIntake >= dailyGoal) {
        println("Congratulations! You have met your daily goal.")
    } else {
        println("You are ${dailyGoal - totalIntake} ml short of your daily goal. Keep it up tomorrow!")
    }
}
