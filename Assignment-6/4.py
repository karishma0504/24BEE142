# Prompt: Create a list of tuples containing a food item and its price.
# Sort the tuples in descending order by price.

# List of food items and their prices (food, price)
food_items = [("Pizza", 12), ("Burger", 5), ("Pasta", 8), ("Salad", 4), ("Sushi", 15)]

# Sort the list by price in descending order (using lambda to specify sorting by the second item of the tuple)
sorted_food_items = sorted(food_items, key=lambda x: x[1], reverse=True)

# Output the sorted list
print("Food items sorted by price (descending):")
for item in sorted_food_items:
    print(f"{item[0]}: ${item[1]}")
