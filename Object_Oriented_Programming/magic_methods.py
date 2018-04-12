class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):  # There's a magic method for every opp sign
        return abs(self.n + other.n)


x = AlwaysPositive(-20)  # first object
y = AlwaysPositive(10)

print(x + y)  # python calls x.__add__(y)
