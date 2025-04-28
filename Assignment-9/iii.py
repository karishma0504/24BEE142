# Prompt: A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string.

# Define the recursive function to count vowels
def count_vowels(s, index=0, count=0):
    # Base case: If the index is at the end of the string, return the count
    if index == len(s):
        return count

    # Check if the character is a vowel
    if s[index].lower() in 'aeiou':
        count += 1

    # Recurse to the next character
    return count_vowels(s, index + 1, count)


# Example usage
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print(f"Number of vowels in the string: {vowel_count}")
