class Horse():
    def __init__(self, col, bre, rid):
        self.color = col
        self.breed = bre
        self.rider = rid
        print("created")


class Rider():
    def __init__(self, nam):
        self.name = nam
        print("created")


mike = Rider("mike smack")
sam = Horse("blue", "stallion", mike)  # Rider object passed as rid parameter

print(sam.rider.name)
