class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if not coins or amount <= 0:
            return 0

        '''
        # DP bottom up O(C*A), 50%
        maxVal = amount+1
        dp = [maxVal]*(amount+1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for c in coins:
                ind = i+c
                if ind > amount:
                    continue
                dp[ind] = min(dp[i]+1, dp[ind])

        # print(dp)
        return dp[-1] if dp[-1] else -1
        '''

        # DFS with memorization O(C*A), 5%
        mem={}
        def helper(remain, memo):
            if remain<0:
                return float('inf') 
            elif not remain:
                return 0 
            elif remain in memo:
                return memo[remain]
            else: 
                memo[remain] =  min([helper(remain-c, memo)+1 for c in coins])
                return memo[remain]

        result = helper(amount, mem)

        return result if result!=float('inf') else -1
