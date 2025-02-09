import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print(f"Area: {c.area():.2f}")
print(f"Perimeter: {c.perimeter():.2f}")
