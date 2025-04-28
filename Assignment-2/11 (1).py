# Prompt: Given three points (x1, y1), (x2, y2) and (x3, y3), check if all the three points fall on one straight line.

x1, y1 = 1, 2
x2, y2 = 2, 4
x3, y3 = 3, 6

# Check if the slope between (x1, y1) and (x2, y2) is the same as the slope between (x2, y2) and (x3, y3)
slope1 = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else None
slope2 = (y3 - y2) / (x3 - x2) if (x3 - x2) != 0 else None

if slope1 == slope2:
    print("The points lie on the same straight line.")
else:
    print("The points do not lie on the same straight line.")
