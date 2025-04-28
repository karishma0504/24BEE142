# Prompt: Write a program that defines a function compute() that calculates the value of
# n + nn + nnn + nnnn, where n is digit received by the function.
# Test the function for digits 4 to 7.

# Define the function
def compute(n):
    n_str = str(n)
    result = int(n_str) + int(n_str*2) + int(n_str*3) + int(n_str*4)
    return result

# Test the function for digits 4 to 7
for num in range(4, 8):
    print(f"Result for {num}:", compute(num))
