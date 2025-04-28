# Prompt: A positive integer is entered through the keyboard. Write a function to find its binary equivalent.

# Define the function to convert a number to binary
def to_binary(n):
    if n == 0:
        return '0'  # Special case for 0
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary  # Add remainder at the front
        n = n // 2  # Divide n by 2
    return binary

# Example usage
num = int(input("Enter a positive integer: "))
binary_representation = to_binary(num)
print(f"Binary equivalent of {num} is: {binary_representation}")
