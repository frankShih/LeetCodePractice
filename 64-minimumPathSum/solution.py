class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0

        # DP, 30%
        dp = [[None]*len(grid[0]) for i in range(len(grid))]
        # print(dp)
        dp[0][0] = grid[0][0]
        
        
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i-1]+grid[0][i]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]

        return dp[-1][-1]        