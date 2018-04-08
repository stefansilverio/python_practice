# use a class to model oranges and create orange objects w/ diff values
# every object is an instance of a class
# every object has the same attributes defined in class they are an instance of
# methods are functions inside of class. Only call them on object class creates


class Orange():
    def __init__(self, w, c):  # magic method executes when class instantiated
        """weights are in oz"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp


orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 98)  # object that calls method gets passed as parameter automat
print(orange.mold)
