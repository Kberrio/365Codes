#include <stdio.h>

int main() {
    char operation;
    double num1, num2, result;

    do {
        // Prompting the user to enter an operation
        printf("Enter an operation (+, -, *, /) or 'q' to quit: ");
        scanf(" %c", &operation);

        // Checking if the user wants to quit
        if (operation == 'q' || operation == 'Q') {
            printf("Exiting the program.\n");
            break;
        }

        // Prompting the user to enter two numbers
        printf("Enter two numbers: ");
        scanf("%lf %lf", &num1, &num2);

        // Performing the requested operation
        switch (operation) {
            case '+':
                result = num1 + num2;
                printf("Result: %.2lf + %.2lf = %.2lf\n", num1, num2, result);
                break;
            case '-':
                result = num1 - num2;
                printf("Result: %.2lf - %.2lf = %.2lf\n", num1, num2, result);
                break;
            case '*':
                result = num1 * num2;
                printf("Result: %.2lf * %.2lf = %.2lf\n", num1, num2, result);
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                    printf("Result: %.2lf / %.2lf = %.2lf\n", num1, num2, result);
                } else {
                    printf("Error: Division by zero!\n");
                }
                break;
            default:
                printf("Invalid operation!\n");
                break;
        }

    } while (1); // Loop indefinitely until the user decides to quit

    return 0;
}
