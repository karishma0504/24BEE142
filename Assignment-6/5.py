# Prompt: Remove empty tuple(s) from the list of tuples

# Example list with some empty tuples
tuples_list = [("Apple", 5), (), ("Banana", 3), (), ("Orange", 7)]

# Remove empty tuples using list comprehension
filtered_list = [t for t in tuples_list if t]

# Output the list after removing empty tuples
print("List after removing empty tuples:", filtered_list)
