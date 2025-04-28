# Prompt: Delete an element of a tuple

# Example tuple
my_tuple = (10, 20, 30, 40, 50)

# Convert the tuple to a list
temp_list = list(my_tuple)

# Delete the element (let's delete the element at index 2, which is 30)
del temp_list[2]

# Convert the list back to a tuple
modified_tuple = tuple(temp_list)

# Output the modified tuple
print("Original tuple:", my_tuple)
print("Modified tuple after deletion:", modified_tuple)
