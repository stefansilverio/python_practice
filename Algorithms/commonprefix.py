class Solution:
    def __init__(self, strs):
        self.strings = strs

    def longestCommonPrefix(self):
        if not self.strings:
            return ""
            shortest = min(self.strings, key=len)  # get smallest string
            for i, ch in enumerate(shortest):
                for other in self.strings:
                    if other[i] != ch:  # if no other strings share indices
                        return shortest[:i]
            return shortest


solution = Solution(["smotter", "smoke", "smield"])
check = solution.longestCommonPrefix()
print(check)
