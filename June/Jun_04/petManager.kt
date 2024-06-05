fun main() {
    val pets = listOf(
        Cat("Whiskers", 2),
        Dog("Rex", 5),
        Bird("Tweety", 1)
    )

    for (pet in pets) {
        println(pet)
        pet.makeSound()
    }

    val petManager = PetManager()
    petManager.addPet(Cat("Mittens", 3))
    petManager.addPet(Dog("Buddy", 4))
    petManager.addPet(Bird("Polly", 2))

    println("All pets:")
    petManager.listPets()

    println("Older than 2 years:")
    petManager.getOlderPets(2).forEach { println(it) }
}

abstract class Pet(val name: String, val age: Int) {
    abstract fun makeSound()
    override fun toString() = "$name (age: $age)"
}

class Cat(name: String, age: Int) : Pet(name, age) {
    override fun makeSound() = println("Meow!")
}

class Dog(name: String, age: Int) : Pet(name, age) {
    override fun makeSound() = println("Woof!")
}

class Bird(name: String, age: Int) : Pet(name, age) {
    override fun makeSound() = println("Tweet!")
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
}
