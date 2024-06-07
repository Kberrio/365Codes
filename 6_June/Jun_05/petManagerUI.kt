import kotlin.random.Random

fun main() {
    val petManager = PetManager()

    // Add some initial pets
    petManager.addPet(Cat("Whiskers", 2, 100))
    petManager.addPet(Dog("Rex", 5, 100))
    petManager.addPet(Bird("Tweety", 1, 100))

    val gameLoop = GameLoop(petManager)
    gameLoop.start()
}

abstract class Pet(
    val name: String,
    val age: Int,
    var health: Int
) {
    abstract fun makeSound()
    abstract fun feed()
    abstract fun play()

    fun reduceHealth(amount: Int) {
        health -= amount
        if (health < 0) health = 0
    }

    override fun toString() = "$name (age: $age, health: $health)"
}

class Cat(name: String, age: Int, health: Int) : Pet(name, age, health) {
    override fun makeSound() = println("$name says: Meow!")
    override fun feed() {
        health += 10
        println("$name is fed. Health is now $health.")
    }
    override fun play() {
        health -= 5
        println("$name played and lost some energy. Health is now $health.")
    }
}

class Dog(name: String, age: Int, health: Int) : Pet(name, age, health) {
    override fun makeSound() = println("$name says: Woof!")
    override fun feed() {
        health += 15
        println("$name is fed. Health is now $health.")
    }
    override fun play() {
        health -= 10
        println("$name played and lost some energy. Health is now $health.")
    }
}

class Bird(name: String, age: Int, health: Int) : Pet(name, age, health) {
    override fun makeSound() = println("$name says: Tweet!")
    override fun feed() {
        health += 5
        println("$name is fed. Health is now $health.")
    }
    override fun play() {
        health -= 2
        println("$name played and lost some energy. Health is now $health.")
    }
}

class PetManager {
    private val pets = mutableListOf<Pet>()

    fun addPet(pet: Pet) {
        pets.add(pet)
    }

    fun listPets() {
        pets.forEach { println(it) }
    }

    fun getOlderPets(age: Int): List<Pet> {
        return pets.filter { it.age > age }
    }

    fun findPetByName(name: String): Pet? {
        return pets.find { it.name == name }
    }

    fun interactWithPets() {
        for (pet in pets) {
            pet.makeSound()
        }
    }

    fun randomEvent() {
        val randomPet = pets[Random.nextInt(pets.size)]
        val eventType = Random.nextInt(3)
        when (eventType) {
            0 -> {
                randomPet.reduceHealth(10)
                println("Random event: ${randomPet.name} got sick and lost 10 health. Health is now ${randomPet.health}.")
            }
            1 -> {
                randomPet.feed()
                println("Random event: ${randomPet.name} found extra food and gained health. Health is now ${randomPet.health}.")
            }
            2 -> {
                randomPet.play()
                println("Random event: ${randomPet.name} played extra and lost some energy. Health is now ${randomPet.health}.")
            }
        }
    }
}

class GameLoop(private val petManager: PetManager) {
    fun start() {
        while (true) {
            println("Pet Management System")
            println("1. List all pets")
            println("2. Interact with pets")
            println("3. Feed a pet")
            println("4. Play with a pet")
            println("5. Quit")

            when (readLine()!!.toInt()) {
                1 -> petManager.listPets()
                2 -> petManager.interactWithPets()
                3 -> {
                    println("Enter the name of the pet to feed:")
                    val name = readLine()!!
                    val pet = petManager.findPetByName(name)
                    pet?.feed() ?: println("Pet not found.")
                }
                4 -> {
                    println("Enter the name of the pet to play with:")
                    val name = readLine()!!
                    val pet = petManager.findPetByName(name)
                    pet?.play() ?: println("Pet not found.")
                }
                5 -> break
                else -> println("Invalid option. Please try again.")
            }

            petManager.randomEvent()
            Thread.sleep(1000)  // Simulate time passing for the pets
        }
    }
}
