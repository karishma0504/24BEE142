# Prompt: Count how many vowels are there in a string. Accept the string from the user

string = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print(f"The number of vowels in the string is {count}")
