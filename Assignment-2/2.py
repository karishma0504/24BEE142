# Prompt: Print largest and smallest values out of three

a = 12
b = 7
c = 20

# Finding largest
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

# Finding smallest
smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

print(f"The largest value is {largest}")
print(f"The smallest value is {smallest}")
