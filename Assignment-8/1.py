# Prompt: Write a program that converts words present in a list into uppercase and stores them in a set

# Example list of words
words_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Convert the words to uppercase and store them in a set
words_set = {word.upper() for word in words_list}

# Output the set of uppercase words
print("Set of uppercase words:", words_set)
