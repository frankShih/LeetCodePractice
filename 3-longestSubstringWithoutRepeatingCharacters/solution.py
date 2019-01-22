class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        # sliding window that keeps track of currentBest O(N^2)
        curSet = set()
        curInd = [0, 0]
        bestInd = [0, 0]

        for i in range(len(s)):
            if not s[i] in curSet:
                curInd[1] += 1
                curSet.add(s[i])

                if curInd[1]-curInd[0] > bestInd[1]-bestInd[0]:
                    bestInd = curInd
            else:
                for j in range(i-1, -1, -1):
                    if s[j] == s[i]:
                        curSet = set(s[j+1:i+1])
                        curInd = [j+1, i+1]
                        break

        return bestInd[1]-bestInd[0]
        '''

        # sliding window, keep last index of each char O(N)
        # using dict, since the range of char isn't given
        indDict = {}
        startInd = result= 0
        for i, c in enumerate(s):
            # duplicate occurred, move startInd
            if c in indDict and startInd <= indDict[c]:
                startInd = indDict[c]+1
            else:
                result= max(result, i-startInd+1)
            indDict[c] = i
        
        return result
        '''
