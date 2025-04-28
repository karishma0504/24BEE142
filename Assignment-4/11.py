# Prompt: Calculate sin(x) where x is in radians, using the given formula

import math

# Function to calculate sin(x) using the given series
def sin_x(x):
    sin_value = 0
    n_terms = 10  # Number of terms for the series
    for n in range(n_terms):
        term = ((-1)**n * x**(2*n+1)) / math.factorial(2*n+1)
        sin_value += term
    return sin_value

# Accept angle in degrees, convert to radians
x_deg = float(input("Enter the angle in degrees: "))
x_rad = x_deg * (math.pi / 180)

# Calculate sin(x)
result = sin_x(x_rad)
print(f"sin({x_deg} degrees) = {result}")
