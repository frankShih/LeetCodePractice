class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        def calculateZeroOne(s):
            z, o = 0, 0
            for char in s:
                if char=='0':
                    z+=1
                else:
                    o+=1
            return [z, o]       

        # DP with memory optimization

        dp = [[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            zeros, ones = calculateZeroOne(s)
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i-zeros][j-ones]+1, dp[i][j])

        return dp[-1][-1]            


        