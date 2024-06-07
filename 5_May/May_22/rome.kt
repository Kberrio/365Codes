import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)

    while (true) {
        println("Welcome to the Roman Empire Information Program!")
        println("Please select an option:")
        println("1. Overview of the Roman Empire")
        println("2. Major Emperors")
        println("3. Important Battles")
        println("4. Roman Culture")
        println("5. Exit")

        when (scanner.nextInt()) {
            1 -> printOverview()
            2 -> printMajorEmperors()
            3 -> printImportantBattles()
            4 -> printRomanCulture()
            5 -> {
                println("Thank you for using the Roman Empire Information Program!")
                break
            }
            else -> println("Invalid option, please try again.")
        }
    }
}

fun printOverview() {
    println("The Roman Empire was one of the largest empires in ancient history, spanning from 27 BC to AD 476.")
    println("It was characterized by its vast territorial holdings across Europe, North Africa, and the Middle East.")
    println("The Roman Empire is known for its military prowess, architectural achievements, and contributions to law and governance.")
}

fun printMajorEmperors() {
    println("Major Emperors of the Roman Empire:")
    println("1. Augustus (27 BC - AD 14) - The first emperor of Rome, who established the principate and ushered in the Pax Romana.")
    println("2. Nero (AD 54 - 68) - Known for his tyrannical rule and the Great Fire of Rome.")
    println("3. Trajan (AD 98 - 117) - Expanded the empire to its greatest territorial extent.")
    println("4. Constantine the Great (AD 306 - 337) - The first Christian emperor, who founded Constantinople.")
}

fun printImportantBattles() {
    println("Important Battles of the Roman Empire:")
    println("1. Battle of Actium (31 BC) - Octavian defeated Mark Antony and Cleopatra, leading to the rise of the Roman Empire.")
    println("2. Battle of the Teutoburg Forest (AD 9) - A major defeat for Rome, halting its expansion into Germania.")
    println("3. Battle of Milvian Bridge (AD 312) - Constantine defeated Maxentius, paving the way for his sole rule and the spread of Christianity.")
    println("4. Battle of Adrianople (AD 378) - A significant defeat by the Goths, which contributed to the decline of the Western Roman Empire.")
}

fun printRomanCulture() {
    println("Roman Culture:")
    println("1. Language: Latin was the official language, influencing many modern languages.")
    println("2. Architecture: Known for structures like the Colosseum, aqueducts, and Roman roads.")
    println("3. Law: The Roman legal system has influenced modern legal frameworks.")
    println("4. Religion: Initially polytheistic, worshiping gods like Jupiter and Mars. Later, Christianity became the state religion.")
}
