class Web():
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def proper(self, n):
        self.name = n.upper()
        return self.name

    def same_object(self, name, age):
        if name is age:
            print("name equals {}.".format(age))
        else:
            print("x is not {}.".format(age))

    def __repr__(self):
        return self.name


smoke = Web("sam", 6)
print(smoke)
print(smoke.proper("sam"))

print(smoke.same_object)
