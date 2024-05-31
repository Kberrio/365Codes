import numpy as np

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def transpose_matrix(matrix):
    return np.transpose(matrix)

# Example matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matrix 1:")
print_matrix(matrix1)

print("Matrix 2:")
print_matrix(matrix2)

# Addition
result_add = add_matrices(matrix1, matrix2)
print("Addition of Matrix 1 and Matrix 2:")
print_matrix(result_add)

# Subtraction
result_subtract = subtract_matrices(matrix1, matrix2)
print("Subtraction of Matrix 1 and Matrix 2:")
print_matrix(result_subtract)

# Multiplication
result_multiply = multiply_matrices(matrix1, matrix2)
print("Multiplication of Matrix 1 and Matrix 2:")
print_matrix(result_multiply)

# Transposition
result_transpose = transpose_matrix(matrix1)
print("Transpose of Matrix 1:")
print_matrix(result_transpose)
