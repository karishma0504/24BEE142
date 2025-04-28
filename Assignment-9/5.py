# Prompt: Pangram is a sentence that uses every letter of the alphabet.
# Write a program to check whether a given string is pangram or not, through a user-defined function ispangram().
# Test the function with given examples.

# Define the function
def ispangram(s):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(s.lower())

# Test the function
test_string1 = "The quick brown fox jumps over the lazy dog"
test_string2 = "Crazy Fredrick bought many very exquisite opal jewels"

print(f"Is pangram? '{test_string1}':", ispangram(test_string1))
print(f"Is pangram? '{test_string2}':", ispangram(test_string2))
