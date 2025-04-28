# Prompt: Given the coordinates (x, y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt(), pow())

import math

# Circle center and radius
center_x, center_y = 0, 0
radius = 5

# Point coordinates
point_x, point_y = 3, 4

# Calculate the distance from the point to the center of the circle
distance = math.sqrt(pow(point_x - center_x, 2) + pow(point_y - center_y, 2))

# Determine whether the point is inside, on, or outside the circle
if distance < radius:
    print("The point is inside the circle.")
elif distance == radius:
    print("The point is on the circle.")
else:
    print("The point is outside the circle.")
