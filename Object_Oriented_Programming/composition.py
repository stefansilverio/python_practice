# composition allows you establish a relationship between two objects by
# storing object as a variable in another object


class Dog():
    def __init__(self, nam, bree, own):
        self.name = nam
        self.breed = bree
        self.owner = own
        print("created!")


class Person():
    def __init__(self, nam):
        self.name = nam


mick = Person("mick jagger")
stan = Dog("stanley", "Bulldog", mick)  # person object passed as owner param

print(stan.owner.name)  # "." give access to object attributes
