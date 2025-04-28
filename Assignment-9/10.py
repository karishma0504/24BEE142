# Prompt: Write a program that defines a function called frequency() which computes the frequency of words
# present in a string passed to it. The frequencies should be returned in sorted order of words in the string.

# Define the function
def frequency(s):
    words = s.split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    sorted_freq = dict(sorted(freq_dict.items()))
    return sorted_freq

# Example usage
input_string = input("Enter a string: ")
result = frequency(input_string)
print("Word frequencies:", result)
