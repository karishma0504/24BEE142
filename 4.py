import math

class RegularShape:
    def __init__(self, shape_type, *dimensions):
        """
        Initializes the shape with type and relevant dimensions.
        :param shape_type: The type of shape (square, circle, triangle, etc.)
        :param dimensions: The dimensions relevant to the shape (e.g., side length or radius)
        """
        self.shape_type = shape_type.lower()  # Type of the shape (square, circle, etc.)
        self.dimensions = dimensions  # Dimensions relevant to the shape (e.g., side length, radius)

    def perimeter(self):
        """
        Calculates and returns the perimeter/circumference of the shape.
        """
        if self.shape_type == 'square':
            # Perimeter of square: 4 * side_length
            side_length = self.dimensions[0]
            return 4 * side_length
        elif self.shape_type == 'circle':
            # Circumference of circle: 2 * π * radius
            radius = self.dimensions[0]
            return 2 * math.pi * radius
        elif self.shape_type == 'triangle':
            # Perimeter of equilateral triangle: 3 * side_length
            side_length = self.dimensions[0]
            return 3 * side_length
        else:
            return "Perimeter calculation not defined for this shape."

    def area(self):
        """
        Calculates and returns the area of the shape.
        """
        if self.shape_type == 'square':
            # Area of square: side_length^2
            side_length = self.dimensions[0]
            return side_length ** 2
        elif self.shape_type == 'circle':
            # Area of circle: π * radius^2
            radius = self.dimensions[0]
            return math.pi * radius ** 2
        elif self.shape_type == 'triangle':
            # Area of equilateral triangle: (√3 / 4) * side_length^2
            side_length = self.dimensions[0]
            return (math.sqrt(3) / 4) * side_length ** 2
        else:
            return "Area calculation not defined for this shape."


# Example usage

# Create a square with side length 5
square = RegularShape('square', 5)
print("Perimeter of Square:", square.perimeter())
print("Area of Square:", square.area())

# Create a circle with radius 7
circle = RegularShape('circle', 7)
print("\nCircumference of Circle:", circle.perimeter())
print("Area of Circle:", circle.area())

# Create an equilateral triangle with side length 6
triangle = RegularShape('triangle', 6)
print("\nPerimeter of Triangle:", triangle.perimeter())
print("Area of Triangle:", triangle.area())
