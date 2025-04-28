import pickle
from datetime import datetime

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def __str__(self):
        return f"Employee[Code: {self.empcode}, Name: {self.empname}, Date of Joining: {self.doj}, Salary: {self.salary}]"

# Serialize the Employee object to a file
def serialize_employee(employee, filename):
    with open(filename, 'wb') as file:
        pickle.dump(employee, file)
    print(f"Employee data serialized to {filename}")

# Deserialize the Employee object from a file
def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        employee = pickle.load(file)
    return employee

# Example usage

# Creating an Employee object
emp = Employee(101, "John Doe", datetime(2020, 5, 15), 50000)

# Serialize the object
serialize_employee(emp, "employee_data.pkl")

# Deserialize the object
deserialized_emp = deserialize_employee("employee_data.pkl")
print("Deserialized Employee Data:")
print(deserialized_emp)
