# Prompt: Write a program that defines a function count_alpha_digits() that accepts a string
# and calculates the number of alphabets and digits in it. It should return these values as a dictionary.

# Define the function
def count_alpha_digits(s):
    alpha_count = 0
    digit_count = 0
    for char in s:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1
    return {'Alphabets': alpha_count, 'Digits': digit_count}

# Example usage
input_string = input("Enter a string: ")
result = count_alpha_digits(input_string)
print("Count:", result)
