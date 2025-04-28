# Prompt: Create two date tuples and find the number of days between them.

from datetime import datetime

# Date tuples (day, month, year)
date1 = (15, 3, 2020)  # Example date 1 (15th March 2020)
date2 = (25, 9, 2021)  # Example date 2 (25th September 2021)

# Convert date tuples to datetime objects
date1_obj = datetime(date1[2], date1[1], date1[0])
date2_obj = datetime(date2[2], date2[1], date2[0])

# Calculate the difference in days
difference = (date2_obj - date1_obj).days

print(f"Number of days between {date1} and {date2} is {difference} days.")
