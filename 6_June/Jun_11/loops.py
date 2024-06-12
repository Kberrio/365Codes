import random

# Initialize a 3D matrix with random integers
matrix_3d = [[[random.randint(1, 100) for _ in range(5)] for _ in range(4)] for _ in range(3)]

# Print the initial 3D matrix
print("Initial 3D Matrix:")
for layer in matrix_3d:
    for row in layer:
        print(row)
    print()

# Function to perform a complex calculation
def complex_calculation(value):
    return (value ** 2 + value) // 2

# Apply the complex calculation to each element using nested loops
for i in range(len(matrix_3d)):
    for j in range(len(matrix_3d[i])):
        for k in range(len(matrix_3d[i][j])):
            matrix_3d[i][j][k] = complex_calculation(matrix_3d[i][j][k])

# Print the transformed 3D matrix
print("Transformed 3D Matrix:")
for layer in matrix_3d:
    for row in layer:
        print(row)
    print()

# Flatten the 3D matrix to a 2D matrix
matrix_2d = [element for layer in matrix_3d for row in layer for element in row]

# Print the flattened 2D matrix
print("Flattened 2D Matrix:")
print(matrix_2d)
print()

# Create a set of unique values using a generator expression
unique_values = set(element for element in matrix_2d)

# Print the set of unique values
print("Unique Values:")
print(unique_values)
print()

# Create a dictionary with the frequency of each unique value
frequency_dict = {value: matrix_2d.count(value) for value in unique_values}

# Print the frequency dictionary
print("Frequency Dictionary:")
print(frequency_dict)
print()

# Transpose the 3D matrix (swap layers with rows and columns)
transposed_matrix_3d = [[[matrix_3d[j][i][k] for j in range(len(matrix_3d))] for i in range(len(matrix_3d[0]))] for k in range(len(matrix_3d[0][0]))]

# Print the transposed 3D matrix
print("Transposed 3D Matrix:")
for layer in transposed_matrix_3d:
    for row in layer:
        print(row)
    print()
