# Prompt: A list contains some negative and some positive values. Write a recursive function that sanitizes the list by replacing all negative numbers with 0.

# Define the recursive function to sanitize the list
def sanitize_list(lst, index=0):
    # Base case: If index is equal to the length of the list, return the list
    if index == len(lst):
        return lst

    # If the current element is negative, replace it with 0
    if lst[index] < 0:
        lst[index] = 0

    # Recurse with the next index
    return sanitize_list(lst, index + 1)


# Example usage
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
sanitized_list = sanitize_list(numbers)
print(f"Sanitized list: {sanitized_list}")
