# Prompt: Write a function that removes one string from another string, if present.
# E.g. Onestring = "abcdef", removestring = "cd". The finalstring should contain "abef"

onestring = input("Enter the main string: ")
removestring = input("Enter the string to remove: ")

# Remove the substring if it exists
finalstring = ""
i = 0
while i < len(onestring):
    if onestring[i:i+len(removestring)] == removestring:
        i += len(removestring)
    else:
        finalstring += onestring[i]
        i += 1

print(f"The final string is: {finalstring}")
