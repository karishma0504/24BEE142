# Two lists: one containing numbers from 1 to 6, and other containing numbers from 6 to 1
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]

# Use map and lambda function to add corresponding elements of both lists
result = list(map(lambda x, y: x + y, list1, list2))

# Print the resulting list
print("The resulting list is:", result)
