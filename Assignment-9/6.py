# Prompt: Write a function to create and return a list containing tuples of the form (x, x^2, x^3)
# for all x between 1 and given ending value (both inclusive).

# Define the function
def create_tuples(end_value):
    result = []
    for x in range(1, end_value + 1):
        result.append((x, x**2, x**3))
    return result

# Example usage
ending_value = int(input("Enter ending value: "))
tuple_list = create_tuples(ending_value)

# Print the list
for item in tuple_list:
    print(item)
