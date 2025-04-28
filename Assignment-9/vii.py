# Prompt: Write a recursive function to obtain the average of all numbers present in a given list.

# Define the recursive function to calculate the average
def average_of_list(lst, index=0, total=0):
    # Base case: If index has reached the end of the list, calculate the average
    if index == len(lst):
        # If the list is not empty, return the average (total / length of list)
        return total / len(lst) if lst else 0

    # Add the current element to the total
    total += lst[index]

    # Recurse with the next index
    return average_of_list(lst, index + 1, total)


# Example usage
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
avg = average_of_list(numbers)
print(f"The average of the list is: {avg}")
