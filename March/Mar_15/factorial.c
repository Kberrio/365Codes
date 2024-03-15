#include <stdio.h>

// Function to calculate factorial recursively
unsigned long long factorial(int n) {
    // Base case: factorial of 0 is 1
    if (n == 0)
        return 1;
    // Recursive case: n! = n * (n-1)!
    else
        return n * factorial(n - 1);
}

int main() {
    int num;

    // Input from user
    printf("Enter a non-negative integer: ");
    scanf("%d", &num);

    // Check for negative input
    if (num < 0) {
        printf("Error: Factorial is undefined for negative integers.\n");
        return 1; // Exit with error code
    }

    // Calculate and display factorial
    printf("Factorial of %d is %llu.\n", num, factorial(num));

    return 0;
}
