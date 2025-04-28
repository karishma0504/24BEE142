# Prompt: Accept marks of three subjects. Print total and average along with whether a candidate has passed or failed. If a student secures <= 39 marks in any subject, consider him as fail. Also assign a subject-wise grade based on the given grade table.

def get_grade(marks):
    if marks == 0:
        return "NA"  # Absent
    elif marks <= 39:
        return "F"
    elif 40 <= marks <= 44:
        return "P"
    elif 45 <= marks <= 49:
        return "C"
    elif 50 <= marks <= 54:
        return "B"
    elif 55 <= marks <= 59:
        return "B+"
    elif 60 <= marks <= 69:
        return "A"
    elif 70 <= marks <= 79:
        return "A+"
    elif 80 <= marks <= 100:
        return "O"

# Accept marks for three subjects
marks1 = int(input("Enter marks for Subject 1: "))
marks2 = int(input("Enter marks for Subject 2: "))
marks3 = int(input("Enter marks for Subject 3: "))

# Calculate total and average
total = marks1 + marks2 + marks3
average = total / 3

# Check if the student has passed or failed
if marks1 <= 39 or marks2 <= 39 or marks3 <= 39:
    result = "Fail"
else:
    result = "Pass"

# Print total, average, and result
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Result: {result}")

# Print grades for each subject
print(f"Grade for Subject 1: {get_grade(marks1)}")
print(f"Grade for Subject 2: {get_grade(marks2)}")
print(f"Grade for Subject 3: {get_grade(marks3)}")
