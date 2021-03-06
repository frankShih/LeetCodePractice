class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        if not amount:
            return 1

        if not coins:
            return 0

        '''
        dp = [0]*(amount+1)
        dp[0]=1
        # coin with permutation case
        # for i in range(amount):
        #     for c in coins:
        #         ind = c+i
        #         if ind>amount:
        #             continue

        #         dp[ind] += dp[i]


        # coin with combination case
        for c in coins:
            for i in range(amount-c+1):
                dp[i+c] += dp[i]

            # print(dp)

        return dp[-1]
        '''

        # timeout solution. need memorizing
        coins = sorted(coins)
        numCoin = len(coins)
        def helper(remain, ind, count):
            if not remain:
                return 1
            if remain<0:
                return 0

            result = 0
            for i in range(ind, numCoin):
                result+=helper(remain-coins[i], i, count+1)

            return result

        return helper(amount, 0, 0)

