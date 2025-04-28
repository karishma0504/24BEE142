# Prompt: Write a recursive function to obtain the length of a given string.

# Define the recursive function to calculate the length of a string
def string_length(s):
    # Base case: If the string is empty, return 0
    if s == "":
        return 0

    # Recursive case: 1 + the length of the substring excluding the first character
    return 1 + string_length(s[1:])


# Example usage
input_string = input("Enter a string: ")
length = string_length(input_string)
print(f"The length of the string is: {length}")
