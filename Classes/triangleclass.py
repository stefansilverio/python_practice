class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("created!")

    def calculate_area(self):
        return (self.base * self.height) / 2


a_trgl = Triangle(6, 8)
print(a_trgl.calculate_area())
