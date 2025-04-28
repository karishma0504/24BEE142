# Prompt: Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees

# List of temperatures in Fahrenheit
fahrenheit = [32, 68, 77, 86, 104]
print("Temperatures in Fahrenheit:", fahrenheit)

# Convert each temperature to Celsius
celsius = [(f - 32) * 5/9 for f in fahrenheit]
print("Temperatures in Celsius:", celsius)
