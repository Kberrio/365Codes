func bubbleSort(_ array: inout [Int]) {
    let n = array.count
    
    for i in 0..<n {
        for j in 0..<(n - i - 1) {
            if array[j] > array[j + 1] {
                array.swapAt(j, j + 1)
            }
        }
    }
}

// Example usage:
var numbers = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(&numbers)
print(numbers)