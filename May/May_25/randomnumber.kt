import io.ktor.application.*
import io.ktor.http.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import kotlin.random.Random

fun main() {
    embeddedServer(Netty, port = 8080) {
        routing {
            get("/random") {
                val randomNumber = generateRandomNumber()
                call.respondText("Random number: $randomNumber", ContentType.Text.Plain)
            }
        }
    }.start(wait = true)
}

fun generateRandomNumber(): Int {
    return Random.nextInt(1, 100)
}
