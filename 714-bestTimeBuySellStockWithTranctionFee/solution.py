class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        length = len(prices)
        if not prices or length<2:
            return 0

        '''
        # treat it as state machine 
        # buy -> sell -> buy
        buy, sell = [0]*length, [0]*length
        buy[0] = -prices[0] 
        sell[0] = 0
        # the max profit that ends with rest/buy/sell operation
        for i in range(1, length):
            price = prices[i]
            buy[i] = max(sell[i-1]-price, buy[i-1])
            sell[i] = max(buy[i-1]+price-fee, sell[i-1]) 
            # print(buy[i], sell[i])
        return max(sell[-1], buy[-1])
        '''

        ans = 0
        minimum = prices[0]
        for i in range(1, length):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i] - fee - minimum
                # min with threshold:'fee', since transaction cause cost
                minimum = prices[i] - fee
        return ans
