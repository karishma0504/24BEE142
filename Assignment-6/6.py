# Prompt: Modify an element of a tuple

# Example tuple
my_tuple = (10, 20, 30, 40)

# Convert the tuple to a list
temp_list = list(my_tuple)

# Modify an element (let's change the second element, index 1)
temp_list[1] = 25

# Convert the list back to a tuple
modified_tuple = tuple(temp_list)

# Output the modified tuple
print("Original tuple:", my_tuple)
print("Modified tuple:", modified_tuple)
