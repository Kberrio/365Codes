function factorial(number) {
    if (number === 0 || number === 1) {
      return 1;
    } else {
      let result = 1;
      for (let i = 2; i <= number; i++) {
        result *= i;
      }
      return result;
    }
  }
  
  // Test cases
  console.log(factorial(5)); // Should print 120
  console.log(factorial(0)); // Should print 1
  console.log(factorial(10)); // Should print 3628800
  