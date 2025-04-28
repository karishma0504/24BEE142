# Prompt: Generate 50 random numbers between 1 and 30, and remove all duplicate values

import random

# Generate 50 random numbers
nums = [random.randint(1, 30) for _ in range(50)]
print("Original list with duplicates:", nums)

# Remove duplicates by converting list to a set, then back to list
unique_nums = list(set(nums))
print("List after removing duplicates:", unique_nums)
