import math


class Circle():
    def __init__(self, r):
        self.radius = r

    def calculate_area(self):
        return self.radius ** 2 * math.pi


a_circle = Circle(5)  # scope of r applies to all methods in class
print(a_circle.calculate_area())
