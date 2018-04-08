#  ability to present the same interface for different data types
#  interface is a function or method
"""

print("hello world!")
print(300)
print(300.1)
print(type(3))

"""
#  able to use print function interface to print them all


#  do not run

class Trl():
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("created!")

    def draw(self):
        return self.base * self.height


class Swl():
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("created!")

    def draw(self):
        return self.base * self.height


class Crl():
    def __init__(self, r):
        self.radius = r
        print("created!")

    def draw(self):
        return self.radius + 1


shapes = [Trl, Swl, Crl]

for a_shape in shapes:
    a_shape.draw()
