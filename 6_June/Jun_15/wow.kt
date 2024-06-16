open class WoWClass(val name: String, val health: Int, val mana: Int) {
    open fun attack() {
        println("$name attacks!")
    }

    open fun useAbility() {
        println("$name uses a basic ability.")
    }

    open fun getInfo() {
        println("Class: $name, Health: $health, Mana: $mana")
    }
}

class Warrior(name: String) : WoWClass(name, 150, 50) {
    override fun attack() {
        println("$name swings a mighty sword!")
    }

    override fun useAbility() {
        println("$name uses Charge!")
    }
}

class Mage(name: String) : WoWClass(name, 100, 200) {
    override fun attack() {
        println("$name casts a fireball!")
    }

    override fun useAbility() {
        println("$name uses Frost Nova!")
    }
}

class Hunter(name: String) : WoWClass(name, 120, 100) {
    override fun attack() {
        println("$name shoots an arrow!")
    }

    override fun useAbility() {
        println("$name uses Steady Shot!")
    }
}

fun main() {
    val warrior = Warrior("Grommash")
    val mage = Mage("Jaina")
    val hunter = Hunter("Sylvanas")

    val characters = listOf<WoWClass>(warrior, mage, hunter)

    for (character in characters) {
        character.getInfo()
        character.attack()
        character.useAbility()
        println()
    }
}
