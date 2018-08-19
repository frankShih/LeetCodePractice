class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        
        start, end = 0, len(s)-1

        while start<end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                # 22%
                return self.isPalindrome(s[:start] + s[(start+1):]) or self.isPalindrome(s[:end] + s[(end+1):]) 
                # 56%
                return self.isPalindrome(s[start:end-1+1]) or self.isPalindrome(s[start+1:end+1]) 
        return True


    def isPalindrome(self, s):
        start, end = 0, len(s)-1

        while start<end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                return False
        return True