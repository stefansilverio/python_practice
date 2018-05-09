class Solution():
    def __init__(self, targ):
        self.target = targ
        self.list = [2, 7, 11, 15]

    def twoSum(self):
        if len(self.list) <= 1:
            return False
        else:
            for i in range(len(self.list)):
                for y in range(len(self.list)):
                    if self.list[y] == self.target - self.list[i]:
                        print(self.list[i], self.list[y])


solution = Solution(9)
solution.twoSum()
