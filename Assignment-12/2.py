class Matrix:
    def __init__(self, data):
        # Initialize the matrix with a 2D list (3x3 matrix)
        self.data = data

    def __add__(self, other):
        # Matrix addition: Adds corresponding elements of two matrices
        result = [[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __mul__(self, other):
        # Matrix multiplication: Multiplies two 3x3 matrices
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return Matrix(result)

    def transpose(self):
        # Matrix transpose: Flips rows and columns
        result = [[self.data[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def display(self):
        # Prints the matrix in a readable format
        for row in self.data:
            print(row)

# Example usage:

# Define two 3x3 matrices
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Matrix Addition
print("Matrix 1 + Matrix 2:")
addition_result = matrix1 + matrix2
addition_result.display()

# Matrix Multiplication
print("\nMatrix 1 * Matrix 2:")
multiplication_result = matrix1 * matrix2
multiplication_result.display()

# Matrix Transpose of matrix1
print("\nTranspose of Matrix 1:")
transpose_result = matrix1.transpose()
transpose_result.display()
