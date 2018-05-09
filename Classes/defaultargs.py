def f(a, L=[]):
    L.append(a)  # array fills up
    return L


print(f(1))
print(f(2))
print(f(3))


def f(a, L=None):  # default gets evaluated once
    if L is None:
        L = []  # array gets re-initialised to empty array everytime
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))
