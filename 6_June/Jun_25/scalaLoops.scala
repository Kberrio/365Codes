object LoopsExample {
  def main(args: Array[String]): Unit = {
    // Using a for loop
    println("Using for loop:")
    for (i <- 1 to 10) {
      println(i)
    }

    // Using a while loop
    println("Using while loop:")
    var j = 1
    while (j <= 10) {
      println(j)
      j += 1
    }
  }
}
