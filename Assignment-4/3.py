# Prompt: Count number of alphabets and number of digits in any given string

string = input("Enter a string: ")

alphabets = 0
digits = 0

for char in string:
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        alphabets += 1
    elif '0' <= char <= '9':
        digits += 1

print(f"Number of alphabets: {alphabets}")
print(f"Number of digits: {digits}")
