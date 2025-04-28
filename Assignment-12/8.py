class String:
    def __init__(self, value=""):
        """Initialize the String object with a given value."""
        self.value = value

    def __iadd__(self, other):
        """Overload the += operator to concatenate two strings."""
        if isinstance(other, String):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        return self

    def toLower(self):
        """Convert all characters of the string to lowercase."""
        self.value = self.value.lower()
        return self

    def toUpper(self):
        """Convert all characters of the string to uppercase."""
        self.value = self.value.upper()
        return self

    def __str__(self):
        """Return the string representation of the String object."""
        return self.value

# Example usage:
str1 = String("Hello")
str2 = String(" World")

# Concatenating using overloaded += operator
str1 += str2
print(f"Concatenated String: {str1}")

# Convert to lower case
str1.toLower()
print(f"Lowercase String: {str1}")

# Convert to upper case
str1.toUpper()
print(f"Uppercase String: {str1}")
