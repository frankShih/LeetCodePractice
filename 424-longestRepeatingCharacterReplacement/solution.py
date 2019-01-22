class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        best = 0
        if not s:
            return best

        length = len(s)
        wordCount = [0]*26
        asciiBase = ord('A')
        maxCount = 0
        startInd = 0
        # sliding window, keep moving endInd/startInd & checking O(N)
        for endInd in range(length):
            indS = ord(s[endInd])
            wordCount[indS-asciiBase]+=1
            # get current majority char
            maxCount = max(maxCount, wordCount[indS-asciiBase])

            while endInd-startInd+1>k+maxCount:  
                # exceed threshold 
                # 1. incoming char is not char of maxCount 
                # 2. incoming char is new char of maxCount 
                wordCount[ord(s[startInd])-asciiBase]-=1
                startInd+=1

            best = max(best, endInd-startInd+1)
        return best            
