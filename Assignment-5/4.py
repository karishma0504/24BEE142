# Prompt: Generate 30 random numbers, separate them into positive and negative lists

import random

# Generate 30 random numbers between -50 and 50
nums = [random.randint(-50, 50) for _ in range(30)]
print("Original list:", nums)

# Create positive and negative lists
positive = [x for x in nums if x > 0]
negative = [x for x in nums if x < 0]

print("Positive numbers:", positive)
print("Negative numbers:", negative)
