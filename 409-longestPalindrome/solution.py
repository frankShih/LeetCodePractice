class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        result = 0
        '''
        # naive version
        letterCount = dict()
        for c in s:
            letterCount.setdefault(c, 0)
            letterCount[c]+=1

        haveOdd = False

        for _, v in letterCount.items():
            if v%2:
                haveOdd = True
                result+= (v-1)
            else:
                result+=v

        if haveOdd:
            result+=1

        return result                
        '''

        # more concise form
        import collections
        c = collections.Counter(s)
        for _, v in c.items():
            result+=(v-v%2)

        return result+1 if result<len(s) else result                
