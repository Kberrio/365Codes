import kotlinx.coroutines.*
import java.time.LocalDateTime

fun main() = runBlocking {
    val taskManager = TaskManager()
    taskManager.addTask("Write Report", Priority.HIGH)
    taskManager.addTask("Prepare Presentation", Priority.MEDIUM)
    taskManager.addTask("Send Emails", Priority.LOW)

    taskManager.displayTasks()

    taskManager.completeTask(1)
    taskManager.displayTasks()

    val deferred = async { taskManager.getTaskSummary() }
    println("Task Summary: ${deferred.await()}")
}

enum class Priority {
    LOW, MEDIUM, HIGH
}

data class Task(val id: Int, val name: String, val priority: Priority, val timestamp: LocalDateTime = LocalDateTime.now()) {
    var isCompleted: Boolean = false
}

class TaskManager {
    private val tasks = mutableListOf<Task>()
    private var nextId = 1

    fun addTask(name: String, priority: Priority) {
        val task = Task(nextId++, name, priority)
        tasks.add(task)
        println("Task Added: $task")
    }

    fun completeTask(id: Int) {
        val task = tasks.find { it.id == id }
        task?.let {
            it.isCompleted = true
            println("Task Completed: $it")
        }
    }

    fun displayTasks() {
        println("Current Tasks:")
        tasks.forEach { task ->
            println("${task.id}: ${task.name} [${task.priority}] - Completed: ${task.isCompleted}")
        }
    }

    suspend fun getTaskSummary(): String {
        delay(1000) // Simulate long-running operation
        val completedTasks = tasks.count { it.isCompleted }
        val pendingTasks = tasks.size - completedTasks
        return "Completed: $completedTasks, Pending: $pendingTasks"
    }
}
