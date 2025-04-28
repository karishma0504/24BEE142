# List containing names of faculty members
faculty_members = ['Johnathan', 'Emily', 'Christopher', 'Sarah', 'Alexander', 'Bob', 'Benjamin']

# Use list comprehension to filter out names with more than 8 characters
filtered_names = [name for name in faculty_members if len(name) > 8]

# Print the filtered list
print("Faculty names with more than 8 characters:", filtered_names)
