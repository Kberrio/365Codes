import re

def calculate(expression, variables={}):
    # Replace variables in the expression with their values
    for var, val in variables.items():
        expression = expression.replace(var, str(val))

    # Use regular expression to validate the expression
    pattern = re.compile(r'[^0-9+\-*/().\s]')
    if pattern.search(expression):
        return "Invalid expression"

    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Division by zero error"
    except Exception as e:
        return f"Error: {e}"

# Example usage:
expression = "2 * (3 + x)"
variables = {"x": 5}
print(calculate(expression, variables))
