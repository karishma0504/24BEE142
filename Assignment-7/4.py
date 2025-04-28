# Prompt: Write a program that reads a string from the keyboard and creates a dictionary
# containing frequency of each character occurring in the string.

# Read a string from the user
input_string = input("Enter a string: ")

# Initialize an empty dictionary to store character frequencies
char_frequency = {}

# Loop through each character in the string
for char in input_string:
    # If character is already in the dictionary, increment its count
    if char in char_frequency:
        char_frequency[char] += 1
    # If character is not in the dictionary, add it with count 1
    else:
        char_frequency[char] = 1

# Output the frequency of each character
print("Character frequency in the string:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")
