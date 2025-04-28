# Prompt: Print all alphabets in upper case and in lower case

# Print uppercase letters
print("Uppercase Letters:")
for i in range(65, 91):  # ASCII values for A-Z
    print(chr(i), end=" ")
print()

# Print lowercase letters
print("Lowercase Letters:")
for i in range(97, 123):  # ASCII values for a-z
    print(chr(i), end=" ")
print()
