import random

def generate_hex_matrix(rows, cols):
    """Generates a matrix of random hexadecimal values."""
    matrix = []
    for _ in range(rows):
        row = [format(random.randint(0, 255), '02x') for _ in range(cols)]
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    """Prints the matrix in a readable format."""
    for row in matrix:
        print(" ".join(row))

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    hex_matrix = generate_hex_matrix(rows, cols)
    print("Generated Hexadecimal Matrix:")
    print_matrix(hex_matrix)

if __name__ == "__main__":
    main()
