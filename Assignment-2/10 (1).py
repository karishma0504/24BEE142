# Prompt: Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter.

length = 10
breadth = 5

area = length * breadth
perimeter = 2 * (length + breadth)

if area > perimeter:
    print("The area of the rectangle is greater than its perimeter.")
else:
    print("The area of the rectangle is not greater than its perimeter.")
