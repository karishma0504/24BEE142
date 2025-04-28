# Prompt: Calculate a^b where a and b are received through the keyword using recursion.

# Define the recursive function to calculate a^b
def power(a, b):
    # Base case: If b is 0, return 1 (as a^0 = 1)
    if b == 0:
        return 1
    # Recursive case: a^b = a * a^(b-1)
    return a * power(a, b - 1)

# Example usage
a = int(input("Enter the base number (a): "))
b = int(input("Enter the exponent (b): "))
result = power(a, b)
print(f"{a} raised to the power of {b} is: {result}")
