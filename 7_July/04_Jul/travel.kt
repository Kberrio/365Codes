import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

data class TravelEvent(
    val name: String,
    val startTime: LocalDateTime,
    val endTime: LocalDateTime,
    val location: String
)

class TravelScheduler {
    private val events = mutableListOf<TravelEvent>()

    fun addEvent(event: TravelEvent) {
        events.add(event)
        events.sortBy { it.startTime }
    }

    fun removeEvent(name: String) {
        events.removeAll { it.name == name }
    }

    fun getEvents(): List<TravelEvent> = events.toList()

    fun printSchedule() {
        val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")
        events.forEach { event ->
            println("Event: ${event.name}")
            println("Location: ${event.location}")
            println("Start: ${event.startTime.format(formatter)}")
            println("End: ${event.endTime.format(formatter)}")
            println("-----------------")
        }
    }
}

fun main() {
    val scheduler = TravelScheduler()

    // Adding some sample events
    scheduler.addEvent(
        TravelEvent(
            "Flight to Paris",
            LocalDateTime.of(2024, 7, 10, 10, 0),
            LocalDateTime.of(2024, 7, 10, 14, 0),
            "Airport"
        )
    )
    scheduler.addEvent(
        TravelEvent(
            "Eiffel Tower Visit",
            LocalDateTime.of(2024, 7, 11, 9, 0),
            LocalDateTime.of(2024, 7, 11, 12, 0),
            "Eiffel Tower, Paris"
        )
    )

    // Print the schedule
    scheduler.printSchedule()
}