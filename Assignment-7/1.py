# Prompt: Write a program to create three dictionaries and concatenate them to create a fourth dictionary

# Creating three dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

# Concatenate the dictionaries to create the fourth dictionary
dict4 = {**dict1, **dict2, **dict3}

# Output the concatenated dictionary
print("Fourth Dictionary:", dict4)
