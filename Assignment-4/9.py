# Prompt: Print N natural numbers in reverse

N = int(input("Enter a number N: "))

# Print natural numbers in reverse order
for i in range(N, 0, -1):
    print(i, end=" ")
