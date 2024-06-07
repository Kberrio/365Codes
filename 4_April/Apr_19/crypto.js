const crypto = require('crypto');

// Function to generate a cryptographically secure random number
function generateSecureRandomNumber(min, max) {
  const range = max - min + 1;
  const bytesNeeded = Math.ceil(Math.log2(range) / 8);
  const randomBytes = crypto.randomBytes(bytesNeeded);
  const randomValue = randomBytes.readUIntBE(0, bytesNeeded);
  const normalizedRandom = randomValue / Math.pow(2, 8 * bytesNeeded);
  return Math.floor(normalizedRandom * range) + min;
}

// Function to perform some complex mathematical operations
function performComplexMathOperation(num) {
  // Example complex operation: finding the factorial of a number
  let factorial = 1;
  for (let i = 2; i <= num; i++) {
    factorial *= i;
  }
  // Example: Finding the square root of the factorial
  const squareRoot = Math.sqrt(factorial);
  // Example: Raising the square root to the power of the original number
  const result = Math.pow(squareRoot, num);
  return result;
}

// Generate a cryptographically secure random number between 1000 and 9999
const randomNumber = generateSecureRandomNumber(1000, 9999);

// Perform complex mathematical operations on the random number
const complexResult = performComplexMathOperation(randomNumber);

// Log the result
console.log("Random number:", randomNumber);
console.log("Complex result:", complexResult);