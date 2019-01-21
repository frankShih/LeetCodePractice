class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
	    # 90%, bottom up
        earning = 0

        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                earning += (prices[i+1]-prices[i])

        return earning