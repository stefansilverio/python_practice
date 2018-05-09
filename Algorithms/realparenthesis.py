class Solution:
    def isvalid(self, s):
        """
        type s: str
        rtype: bool
        """
        q = []
        for w in s:
            if w == '(':
                q.append(')')
             w == '[':
                q.append(']')
            elif w == '{':
                q.append('}')
            elif not q or (q and q.pop() != w):
                return False
        return not q


solution = Solution()
bob = solution.isvalid("[]")
print(bob)
