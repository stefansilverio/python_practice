class Apple():
    def __init__(self, s, c, w, g):
        self.shape = s
        self.color = c
        self.weight = w
        self.girth = g

    def ripen(self):
        return self.girth * self.weight


aapl = Apple("round", "red", 4, 2)  # Instantiating class
aapl.ripen()  # calling method on class
print(aapl.ripen)
