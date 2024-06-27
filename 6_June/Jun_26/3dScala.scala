object ThreeDArrayExample {
  def main(args: Array[String]): Unit = {
    // Initialize a 3D array with dimensions 2x2x2
    val array3D = Array.ofDim[Int](2, 2, 2)

    // Fill the 3D array with values
    for (i <- 0 until 2) {
      for (j <- 0 until 2) {
        for (k <- 0 until 2) {
          array3D(i)(j)(k) = i * 4 + j * 2 + k
        }
      }
    }

    // Print the 3D array
    println("3D Array values and their coordinates:")
    for (i <- 0 until 2) {
      for (j <- 0 until 2) {
        for (k <- 0 until 2) {
          println(s"array3D($i)($j)($k) = ${array3D(i)(j)(k)}")
        }
      }
    }
  }
}
