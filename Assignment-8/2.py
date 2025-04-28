import random

# Create a set containing 10 random numbers in the range 15 to 45
random_numbers = {random.randint(15, 45) for _ in range(10)}

# Count how many numbers are less than 30
count_less_than_30 = sum(1 for num in random_numbers if num < 30)

# Remove numbers greater than 35
random_numbers = {num for num in random_numbers if num <= 35}

# Output the results
print("Random numbers:", random_numbers)
print("Count of numbers less than 30:", count_less_than_30)
