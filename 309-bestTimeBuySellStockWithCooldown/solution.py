class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if not prices or length<2:
            return 0

        # treat it as state machine 
        # buy -> rest -> sell -> rest

        buy, sell, rest = [0]*length, [0]*length, [0]*length
        buy[0] = -prices[0] 
        sell[0] = 0
        # the max profit that ends with rest/buy/sell operation
        for i in range(1, length):
            price = prices[i]
            rest[i] = max(sell[i-1], rest[i-1])
            buy[i] = max(rest[i-1]-price, buy[i-1])
            # sell[i] = buy[i-1]+price
            sell[i] = max(buy[i-1]+price, rest[i-1]) 
            # print(buy[i], sell[i], rest[i])
        return max(sell[i], rest[i])


        '''
        # memory optimized version
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            print(buy, sell)
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell
        '''