# Prompt: Write a recursive function that reverses the list of numbers that it receives.

# Define the recursive function to reverse the list
def reverse_list(lst):
    # Base case: If the list is empty or has one element, return the list
    if len(lst) <= 1:
        return lst

    # Recurse: Take the last element and reverse the rest of the list
    return [lst[-1]] + reverse_list(lst[:-1])


# Example usage
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
reversed_numbers = reverse_list(numbers)
print(f"Reversed list: {reversed_numbers}")
