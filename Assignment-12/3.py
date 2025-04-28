import math

class Solid:
    def __init__(self, solid_type, *dimensions):
        # Initialize the solid type and dimensions
        self.solid_type = solid_type.lower()  # type of the solid (sphere, cuboid, etc.)
        self.dimensions = dimensions  # Dimensions relevant to the solid (radius, length, width, height)

    def surface_area(self):
        if self.solid_type == 'sphere':
            # Surface area of a sphere: 4 * π * r^2
            radius = self.dimensions[0]
            return 4 * math.pi * radius ** 2
        elif self.solid_type == 'cuboid':
            # Surface area of a cuboid: 2 * (lw + lh + wh)
            length, width, height = self.dimensions
            return 2 * (length * width + length * height + width * height)
        else:
            return "Surface area calculation not defined for this solid type."

    def volume(self):
        if self.solid_type == 'sphere':
            # Volume of a sphere: (4/3) * π * r^3
            radius = self.dimensions[0]
            return (4/3) * math.pi * radius ** 3
        elif self.solid_type == 'cuboid':
            # Volume of a cuboid: l * w * h
            length, width, height = self.dimensions
            return length * width * height
        else:
            return "Volume calculation not defined for this solid type."

# Example usage

# Create a sphere object with radius 5
sphere = Solid('sphere', 5)
print("Surface Area of Sphere:", sphere.surface_area())
print("Volume of Sphere:", sphere.volume())

# Create a cuboid object with length 4, width 3, and height 2
cuboid = Solid('cuboid', 4, 3, 2)
print("\nSurface Area of Cuboid:", cuboid.surface_area())
print("Volume of Cuboid:", cuboid.volume())
