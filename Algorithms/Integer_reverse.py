class Reverse():
    def __init__(self, x):
        self.number = x

    def reverseint(self):
        s = list(str(self.number))
        if self.number >= 0:
            res = s[::-1]
            num = int(''.join(res))
        else:
            res = s[1:][::-1]  # 2nd sub-string slices first substring created
            num = int(''.join(res))*(-1)
        if num > (2 ** 31) - 1 or num < - (2**31):
            print(0)
        else:
            print(num)


reverse = Reverse(-456)
reverse.reverseint()
