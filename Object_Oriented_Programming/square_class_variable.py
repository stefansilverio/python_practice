class Square():
    square_list = []

    def __init__(self, s1, n):
        self.side = s1
        self.name = n
        self.square_list.append((self.side, self.name))

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side,
                                             self.side,
                                             self.side,
                                             self.side)


a_sql = Square(3, "bob")  # sql is object that calls method
a_sql = Square(4, "chad")
print(Square(5, "ryan"))
print(Square.square_list)
