# Prompt: Create an empty set. Write a program that adds five new names to this set,
# modifies one existing name and deletes two names from it.

# Create an empty set
names_set = set()

# Add five new names to the set
names_set.add("Alice")
names_set.add("Bob")
names_set.add("Charlie")
names_set.add("David")
names_set.add("Eva")

# Output the set after adding names
print("Set after adding names:", names_set)

# Modify one existing name (remove "Bob" and add "Bobby")
if "Bob" in names_set:
    names_set.remove("Bob")
    names_set.add("Bobby")

# Output the set after modification
print("Set after modifying a name:", names_set)

# Delete two names from the set (remove "Alice" and "Eva")
names_set.discard("Alice")
names_set.discard("Eva")

# Output the final set after deletion
print("Set after deleting names:", names_set)
