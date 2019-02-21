class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        # brute force solution O(N^2) 1%

        if not s:
            return False

        length = len(s)
        for i in range(1, length//2+1):
            if length % i:  # length of substring is not right
                continue
            temp = s[:i]
            if not s.replace(temp, ""):
                return True

        return False
        '''

        # awesome solution O(N), 99%
        # if it has repeated substring(at least two) 
        # copy the string twice with 
        #   first one remove first letter
        #   second one remove last letter
        # then we should find original string from the new one 
        return  s in s[1:]+s[:-1]