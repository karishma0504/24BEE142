import pandas as pd

# Read data from an Excel file
file_path = 'students_data.xlsx'  # Path to your Excel file
df = pd.read_excel(file_path)

# Initialize an empty dictionary to store the data
student_dict = {}

# Iterate over the rows of the dataframe
for index, row in df.iterrows():
    roll_no = row['RollNo']
    name = row['Name']
    subject1_marks = row['Subject1']
    subject2_marks = row['Subject2']
    subject3_marks = row['Subject3']

    # Calculate total marks
    total_marks = subject1_marks + subject2_marks + subject3_marks

    # Store the student data in the dictionary
    student_dict[roll_no] = {
        'Name': name,
        'Subject1 Marks': subject1_marks,
        'Subject2 Marks': subject2_marks,
        'Subject3 Marks': subject3_marks,
        'Total Marks': total_marks
    }

# Display the dictionary
print(student_dict)
