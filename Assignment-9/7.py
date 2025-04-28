# Prompt: A palindrome is a word or phrase that reads the same in both directions.
# Write a program that defines a function ispalindrome() which checks whether a given string is a palindrome or not.
# Ignore spaces and case mismatch while checking for palindrome.

# Define the function
def ispalindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
test_string = input("Enter a string: ")
if ispalindrome(test_string):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
