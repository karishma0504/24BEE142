# Prompt: Write a program that defines a function sum_avg() to accept marks of five subjects
# and calculates total and average. It should return directly both values.

# Define the function
def sum_avg():
    marks = []
    for i in range(1, 6):
        m = float(input(f"Enter marks for subject {i}: "))
        marks.append(m)
    total = sum(marks)
    average = total / 5
    return total, average

# Example usage
total_marks, average_marks = sum_avg()

# Print the results
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
