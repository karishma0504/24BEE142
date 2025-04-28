# List containing strings and numbers
lst = ['madam', 'Python', 'malayalam', 12321]

# Function to check if a string is a palindrome
def is_palindrome(word):
    # Check if the word is a string and is equal to its reverse
    if isinstance(word, str) and word == word[::-1]:
        return True
    return False

# Iterate through the list and print the palindromes
for item in lst:
    if is_palindrome(str(item)):  # Convert number to string if needed
        print(f"'{item}' is a palindrome.")
