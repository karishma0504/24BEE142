# Prompt: Create a list of 5 odd integers using random numbers. Similarly, create a list of 4 even integers using random numbers.
# Replace the third element of odd integers with a list of 4 even integers. Flatten, sort, and print the list with appropriate messages.

import random

# Create a list of 5 odd integers
odd_list = []
while len(odd_list) < 5:
    num = random.randint(1, 100)
    if num % 2 != 0:
        odd_list.append(num)
print(f"Original list of 5 odd integers: {odd_list}")

# Create a list of 4 even integers
even_list = []
while len(even_list) < 4:
    num = random.randint(1, 100)
    if num % 2 == 0:
        even_list.append(num)
print(f"List of 4 even integers: {even_list}")

# Replace the third element of odd_list with even_list
odd_list[2] = even_list
print(f"List after replacing third element with even integers list: {odd_list}")

# Flatten the list
flat_list = []
for item in odd_list:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)
print(f"Flattened list: {flat_list}")

# Sort the flattened list
flat_list.sort()
print(f"Sorted list: {flat_list}")
