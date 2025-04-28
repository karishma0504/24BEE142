# Prompt: Print factorial of a given number

num = int(input("Enter a number: "))

# Calculate factorial
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")
