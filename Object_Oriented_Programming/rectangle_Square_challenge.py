class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l
        print("created!")

    def calculate_perimeter(self):
        return self.length * self.width


class Square():
    def __init__(self, s):
        self.side = s
        print("created!")

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, sub):
        return self.side - sub


a_rect = Rectangle(2, 4)
a_sql = Square(6)

print(a_rect.calculate_perimeter())
print(a_sql.calculate_perimeter())
print(a_sql.change_size(4))
