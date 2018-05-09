class Solution:
    def checknum(self, x):
        if x > 0:
            L = list(str(x))
            if L == L[::-1]:
                return 'True'
            else:
                return 'False'


solution = Solution()
bob = solution.checknum(122)
print(bob)
#  can you do it without converting int to str?
