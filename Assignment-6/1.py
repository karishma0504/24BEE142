# Prompt: A list contains names of boys and girls as its elements. Boys' names are stored as tuples.
# Write a program to find out number of boys and girls in the list.

# Example list with boys' names as tuples and girls' names as strings
names_list = [("John", "Mike"), "Alice", "Eva", ("Tom", "James"), "Sophia", ("Liam",)]

# Count boys (tuples) and girls (strings)
boys_count = sum(1 for ele in names_list if isinstance(ele, tuple))
girls_count = sum(1 for ele in names_list if isinstance(ele, str))

print(f"Number of boys: {boys_count}")
print(f"Number of girls: {girls_count}")
