class ComplexNumber:
    def __init__(self, real, imaginary):
        # Initialize the real and imaginary parts
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # Add two complex numbers
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        # Subtract two complex numbers
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        # Multiply two complex numbers
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __truediv__(self, other):
        # Divide two complex numbers
        denominator = other.real**2 + other.imaginary**2
        if denominator == 0:
            raise ValueError("Cannot divide by zero")
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        # Return the string representation of the complex number
        return f"{self.real} + {self.imaginary}i"

# Example usage:

# Create two complex numbers
complex1 = ComplexNumber(3, 2)  # 3 + 2i
complex2 = ComplexNumber(1, 7)  # 1 + 7i

# Perform addition
addition_result = complex1 + complex2
print(f"Addition: {addition_result}")

# Perform subtraction
subtraction_result = complex1 - complex2
print(f"Subtraction: {subtraction_result}")

# Perform multiplication
multiplication_result = complex1 * complex2
print(f"Multiplication: {multiplication_result}")

# Perform division
try:
    division_result = complex1 / complex2
    print(f"Division: {division_result}")
except ValueError as e:
    print(f"Error in division: {e}")
