class Hexagon():
    def __init__(self, l):
        self.length = l
        print("created!")

    def calculate_perimeter(self):
        return self.length * 6


a_hexa = Hexagon(7)
print(a_hexa.calculate_perimeter())
