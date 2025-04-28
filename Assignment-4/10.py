# Prompt: Generate N numbers of Fibonacci series

N = int(input("Enter the number of Fibonacci numbers to generate: "))

# First two numbers of Fibonacci sequence
a, b = 0, 1

# Generate and print the Fibonacci series
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b
