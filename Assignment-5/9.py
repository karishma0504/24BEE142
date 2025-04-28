# Prompt: Take two lists of numbers and create a third list with numbers from the first list that are not in the second list

# Example lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

# Create third list using list comprehension
list3 = [num for num in list1 if num not in list2]

print("First List:", list1)
print("Second List:", list2)
print("Third List (from first list but not in second):", list3)
