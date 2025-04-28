# Prompt: Accept two strings. Check whether one string is there in another string

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if string2 in string1:
    print(f"The string '{string2}' is found in '{string1}'.")
else:
    print(f"The string '{string2}' is not found in '{string1}'.")
