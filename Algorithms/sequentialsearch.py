def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break  # loop stops when you find your variable
    return found  # all in the same function can access variables state


numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)
