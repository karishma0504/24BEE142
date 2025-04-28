# Prompt: Write a program that defines a function create_array() to create and return a 3D array
# whose dimensions are passed to the function. Also initialize each element of this array
# to a value passed to the function.
# e.g. create_array(3,4,5,n) where first three arguments are dimensions and 4th is initial value.

# Define the function
def create_array(x, y, z, value):
    array = [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]
    return array

# Example usage
array_3d = create_array(3, 4, 5, 0)  # 3x4x5 array initialized with 0

# Print the array
for plane in array_3d:
    print(plane)
