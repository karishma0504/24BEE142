class Date:
    def __init__(self, day, month, year):
        """Initialize the Date object with day, month, and year."""
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        """Override the == operator to compare two Date objects."""
        if isinstance(other, Date):
            return (self.day == other.day) and (self.month == other.month) and (self.year == other.year)
        return False  # If the other object is not a Date, return False

    def __str__(self):
        """Return the string representation of the Date."""
        return f"{self.day:02}/{self.month:02}/{self.year}"


# Example usage:
date1 = Date(15, 8, 2022)
date2 = Date(15, 8, 2022)
date3 = Date(1, 1, 2021)

print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Date 3: {date3}")

# Comparison of Date objects
if date1 == date2:
    print("Date 1 and Date 2 are the same.")
else:
    print("Date 1 and Date 2 are different.")

if date1 == date3:
    print("Date 1 and Date 3 are the same.")
else:
    print("Date 1 and Date 3 are different.")
