import math
#İlk Bununla başla...
## Kapsülleme
## Kalıtım
## Çok Biçimlilik
## Soyutlama
# Base class
class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.perimeter_ = self.perimeter()
        self.area_ = self.area()

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Derived class for Triangle
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for shape in shapes:
    print(f"{type(shape).__name__} area: {shape.area():.2f}, perimeter: {shape.perimeter():.2f}")

