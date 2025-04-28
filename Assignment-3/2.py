# Prompt: Write your own functions (without using built-in functions) to convert all characters of a string into lower case / upper case / toggle case

string = input("Enter a string: ")

# Convert to lowercase
lowercase = ""
for char in string:
    if 'A' <= char <= 'Z':
        lowercase += chr(ord(char) + 32)
    else:
        lowercase += char

# Convert to uppercase
uppercase = ""
for char in string:
    if 'a' <= char <= 'z':
        uppercase += chr(ord(char) - 32)
    else:
        uppercase += char

# Toggle case
togglecase = ""
for char in string:
    if 'A' <= char <= 'Z':
        togglecase += chr(ord(char) + 32)
    elif 'a' <= char <= 'z':
        togglecase += chr(ord(char) - 32)
    else:
        togglecase += char

print(f"Lowercase: {lowercase}")
print(f"Uppercase: {uppercase}")
print(f"Togglecase: {togglecase}")
