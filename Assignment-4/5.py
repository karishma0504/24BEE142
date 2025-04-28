# Prompt: Generate all Pythagorean Triplets with side length <= 30

for a in range(1, 31):
    for b in range(a, 31):  # Start from a to avoid duplicates
        c = (a**2 + b**2)**0.5
        if c.is_integer() and c <= 30:
            print(f"({a}, {b}, {int(c)})")
