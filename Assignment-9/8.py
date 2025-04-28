# Prompt: Write a program that defines a function convert() that receives a string containing a sequence of
# whitespace separated words and returns a string after removing all duplicate words and sorting them alphanumerically.

# Define the function
def convert(s):
    words = s.split()
    unique_words = set(words)
    sorted_words = sorted(list(unique_words))
    return ' '.join(sorted_words)

# Example usage
input_string = input("Enter a sequence of words: ")
result = convert(input_string)
print("Processed string:", result)
