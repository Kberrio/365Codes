try:
    # Code that might raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    result = num1 / num2
    
    print("Result:", result)

except ZeroDivisionError:
    # Handle the case where division by zero occurs
    print("Error: Division by zero is not allowed.")

except ValueError:
    # Handle the case where user enters non-integer input
    print("Error: Please enter valid integer numbers.")

except Exception as e:
    # Handle any other unexpected exceptions
    print(f"An unexpected error occurred: {e}")

else:
    # Code to execute if no exception is raised
    print("No exceptions were raised.")

finally:
    # Code that will always execute, regardless of exceptions
    print("Execution completed.")
