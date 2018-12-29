class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        if not m or not n:
            return 0

'''
        # DP, 21%
        dp = [[None]*m for i in range(n)]
        
        dp[0][0] = 1
        
        for i in range(1, n):
            dp[i][0] = 1
        for i in range(1, m):
            dp[0][i] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # print(dp)
        return dp[-1][-1]        
'''

        # combination, 21%
        # m+n-2 choose m-1
        p = m+n-2
		# Taking the min of m and n minimizes the number of loops in the p choose k calculation
        k = min(m,n)-1
        # p Choose k
        tot = 1
        for i in range(k):
            tot*=(p-i)
        for i in range(k):
            tot/=(k-i)
        return int(tot)
