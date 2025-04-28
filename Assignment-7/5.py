# Prompt: Create two dictionaries – one containing grocery items and their prices
# and another containing grocery items and quantity purchased.
# Compute the total bill.

# Dictionary of grocery items and their prices
grocery_prices = {
    "apple": 2.5,   # Price per item
    "banana": 1.2,
    "carrot": 0.8,
    "milk": 1.5,
    "bread": 2.0
}

# Dictionary of grocery items and quantity purchased
grocery_quantities = {
    "apple": 3,     # Quantity purchased
    "banana": 5,
    "carrot": 2,
    "milk": 1,
    "bread": 4
}

# Initialize a variable to store the total bill
total_bill = 0

# Calculate the total bill by multiplying price and quantity for each item
for item in grocery_prices:
    if item in grocery_quantities:
        total_bill += grocery_prices[item] * grocery_quantities[item]

# Output the total bill
print(f"Total Bill: ${total_bill:.2f}")
