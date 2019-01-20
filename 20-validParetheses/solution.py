class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return True

        length = len(s)    
        stack = []
        myDict = {"(":")","[":"]","{":"}" }
        
        for i in range(length):
            if s[i] in myDict:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                
                temp = stack.pop()
                if myDict[temp]!=s[i]:
                    return False

        return not stack
