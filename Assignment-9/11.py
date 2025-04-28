# Prompt: Write a function create_list() that creates and returns a list
# which is an intersection of two lists passed to it.

# Define the function
def create_list(list1, list2):
    # Using set intersection to find common elements
    return list(set(list1) & set(list2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = create_list(list1, list2)
print("Intersection of the two lists:", result)
