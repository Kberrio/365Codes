import Foundation

func factorial(_ n: Int) -> Int {
    if n == 0 {
        return 1
    } else {
        return n * factorial(n - 1)
    }
}

func main() {
    print("Enter a number to calculate its factorial:")
    if let input = readLine(),
       let number = Int(input) {
        let result = factorial(number)
        print("The factorial of \(number) is \(result)")
    } else {
        print("Invalid input. Please enter a valid number.")
    }
}

main()
