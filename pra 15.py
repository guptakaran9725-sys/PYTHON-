# PRACTICAL 15: Matrix Operations

# Function to input a matrix from user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter elements row by row ({rows}x{cols} matrix):")
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Element [{i+1},{j+1}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

# Function to display matrix
def display_matrix(matrix):
    for row in matrix:
        print(row)

# Matrix Addition
def add_matrices(A, B):
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

# Matrix Subtraction
def subtract_matrices(A, B):
    result = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

# Matrix Multiplication
def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Matrix Transpose
def transpose_matrix(A):
    result = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    return result


# -------------------------------
# Example usage
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nMatrix A:")
A = input_matrix(rows, cols)

print("\nMatrix B:")
B = input_matrix(rows, cols)

print("\nMatrix A:")
display_matrix(A)
print("Matrix B:")
display_matrix(B)

print("\nAddition of Matrices:")
display_matrix(add_matrices(A, B))

print("\nSubtraction of Matrices:")
display_matrix(subtract_matrices(A, B))

print("\nMultiplication of Matrices:")
display_matrix(multiply_matrices(A, B))

print("\nTranspose of Matrix A:")
display_matrix(transpose_matrix(A))

print("\nTranspose of Matrix B:")
display_matrix(transpose_matrix(B))