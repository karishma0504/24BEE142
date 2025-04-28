import random

# Generate a list of 10 different random numbers between -15 and 15
random_numbers = random.sample(range(-15, 16), 10)

# Create a new list by squaring each number in the original list
squared_numbers = [x**2 for x in random_numbers]

# Print the original and squared lists
print("Original list of random numbers:", random_numbers)
print("List of squared numbers:", squared_numbers)
