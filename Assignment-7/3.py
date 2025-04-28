# Prompt: Create a dictionary with dept no, employee roll no., and salary.
# Find out department wise minimum and maximum salary.

# Example dictionary with department as the key, and values as lists of tuples (employee roll no., salary)
employee_data = {
    101: [(1, 40000), (2, 50000), (3, 60000)],  # Dept 101: Employee roll no. and salary
    102: [(4, 35000), (5, 45000), (6, 55000)],  # Dept 102
    103: [(7, 70000), (8, 80000), (9, 60000)]  # Dept 103
}

# Find department wise min and max salary
for dept_no, employees in employee_data.items():
    # Extract salaries from the list of tuples
    salaries = [salary for _, salary in employees]

    # Calculate min and max salary
    min_salary = min(salaries)
    max_salary = max(salaries)

    print(f"Department {dept_no}: Min Salary = {min_salary}, Max Salary = {max_salary}")
