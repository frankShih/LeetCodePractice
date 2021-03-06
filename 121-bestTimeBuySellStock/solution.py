class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        best = 0
        # greedy solution with sliding window O(N)
        cur_min = prices[0]
        for p in prices:
            if p > cur_min:
                best = max(best, p - cur_min)
            else:
                # move startInd to 'i' (values before it are too large to be candidate
                cur_min = p

        return best