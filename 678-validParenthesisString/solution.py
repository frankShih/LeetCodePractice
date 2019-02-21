class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not s:
            return True

        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0