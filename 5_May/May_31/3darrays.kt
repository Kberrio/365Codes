fun main() {
    // Define the dimensions of the array
    val rows = 3
    val cols = 4

    // Create a 2D array with the specified dimensions
    val array = Array(rows) { IntArray(cols) }

    // Fill the array with values
    for (i in 0 until rows) {
        for (j in 0 until cols) {
            array[i][j] = i * j
        }
    }

    // Print the array
    for (i in 0 until rows) {
        for (j in 0 until cols) {
            print("${array[i][j]} ")
        }
        println()
    }
}
