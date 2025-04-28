# Prompt: Generate 20 random integers, accept a number, and print positions of all its occurrences

import random

# Generate list of 20 random integers between 1 and 50
nums = [random.randint(1, 50) for _ in range(20)]
print("Generated List:", nums)

# Accept number from user
n = int(input("Enter a number to find its positions: "))

# Find and print all positions
positions = [i for i, val in enumerate(nums) if val == n]

if positions:
    print(f"The number {n} found at positions:", positions)
else:
    print(f"The number {n} is not found in the list.")
