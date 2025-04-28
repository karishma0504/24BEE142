# Prompt: Write a program that defines a function count_lower_upper()
# that accepts a string and calculates the number of uppercase and lowercase alphabets in it.
# It should return these values as a dictionary. Call this function for some sample string.

# Define the function
def count_lower_upper(s):
    result = {"uppercase": 0, "lowercase": 0}
    for char in s:
        if char.isupper():
            result["uppercase"] += 1
        elif char.islower():
            result["lowercase"] += 1
    return result

# Sample string
sample_text = "Hello World! This is Python 123."

# Call the function and store the result
counts = count_lower_upper(sample_text)

# Output the result
print("Counts:", counts)
