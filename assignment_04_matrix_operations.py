# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# Helper function to read a matrix from user input
def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} values. Please re-enter row {i + 1}.")
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix

#Helper function to display a matrix in a neat grid format
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:4d}" for val in row))

#PART A — Transpose a Matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    #Create empty result grid (cols x rows)
    transposed = [[0] * rows for _ in range(cols)]

    #Swap rows and columns
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

#PART B — Add Two Matrices
def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    #Create result grid initialized with zeros 
    result = [[0] * cols for _ in range(rows)]

    #Compute element-wise sum
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result

#PART C — Multiply Two Matrices
def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    #Create result grid initialized with zeros (rows_a x cols_b)
    result = [[0] * cols_b for _ in range(rows_a)]

    #Compute matrix product
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):  # or range(rows_b), since cols_a == rows_b
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

#Main Interactive Program Execution
if __name__ == "__main__":
    print("=== PART A: Transpose a Matrix ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))

    matrix = read_matrix(m, n)
    print("\nOriginal Matrix:")
    print_matrix(matrix)

    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    print("\n" + "=" * 35)
    print("=== PART B: Add Two Matrices ===")
    m = int(input("Enter number of rows for matrices: "))
    n = int(input("Enter number of columns for matrices: "))
    
    print("\nEnter Matrix A:")
    mat_a = read_matrix(m, n)
    
    print("\nEnter Matrix B:")
    mat_b = read_matrix(m, n)
    
    sum_result = add_matrices(mat_a, mat_b)
    print("\nMatrix Sum (A + B):")
    print_matrix(sum_result)

    print("\n" + "=" * 35)
    print("=== PART C: Multiply Two Matrices ===")
    m = int(input("Enter number of rows for Matrix A (M): "))
    n = int(input("Enter number of columns for Matrix A / rows for Matrix B (N): "))
    p = int(input("Enter number of columns for Matrix B (P): "))
    
    print(f"\nEnter Matrix A ({m}x{n}):")
    mat_a = read_matrix(m, n)
    
    print(f"\nEnter Matrix B ({n}x{p}):")
    mat_b = read_matrix(n, p)
    
    prod_result = multiply_matrices(mat_a, mat_b)
    print("\nMatrix Product (A x B):")
    print_matrix(prod_result)