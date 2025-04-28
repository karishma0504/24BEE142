# Prompt: A set contains names which begin either with A or with B.
# Write a program to separate out the names into two sets, one containing names beginning with A and another with B.

# Example set containing names
names_set = {"Alice", "Bob", "Anna", "Brian", "David", "Ben", "Ava", "Bella"}

# Create two sets for names beginning with 'A' and 'B'
names_start_with_A = {name for name in names_set if name.startswith('A')}
names_start_with_B = {name for name in names_set if name.startswith('B')}

# Output the sets
print("Names starting with A:", names_start_with_A)
print("Names starting with B:", names_start_with_B)
