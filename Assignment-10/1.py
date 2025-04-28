import csv

# Data to be written to the CSV file
data = [
    ['Name', 'Age', 'Department'],
    ['Alice', 30, 'HR'],
    ['Bob', 25, 'IT'],
    ['Charlie', 35, 'Finance'],
    ['David', 40, 'Marketing']
]

# Open a new CSV file in write mode
with open('faculty_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the data to the CSV file
    writer.writerows(data)

print("CSV file 'faculty_data.csv' has been created successfully.")
