# Prompt: A list contains tuples containing roll no., name, and age of student.
# Write a program to create three lists separately for roll no., name, and age.

# Example list of tuples (roll no., name, age)
students = [(1, "John", 18), (2, "Alice", 20), (3, "Bob", 19), (4, "Eva", 21)]

# Create separate lists for roll no., name, and age
roll_no = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]

# Output the lists
print("Roll Numbers:", roll_no)
print("Names:", names)
print("Ages:", ages)
