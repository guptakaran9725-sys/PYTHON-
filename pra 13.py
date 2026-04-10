# PRACTICAL 13: Demonstrating Method Overloading with Area class

class Area:
    # Method to find area of different shapes
    def find_area(self, *args):
        if len(args) == 1:
            # Circle: area = πr^2
            radius = args[0]
            return 3.14159 * radius * radius

        elif len(args) == 2:
            # Rectangle: area = length * breadth
            length, breadth = args
            return length * breadth

        elif len(args) == 3:
            # Triangle: area = 0.5 * base * height
            base, height, _ = args  # third argument ignored for demonstration
            return 0.5 * base * height

        else:
            return "Invalid number of arguments!"

# -------------------------------
# Example usage
shape = Area()

# Circle area
print("Area of Circle (r=5):", shape.find_area(5))

# Rectangle area
print("Area of Rectangle (l=10, b=4):", shape.find_area(10, 4))

# Triangle area
print("Area of Triangle (base=6, height=3):", shape.find_area(6, 3, 0))