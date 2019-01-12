class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        if not A: return 0
        
        length = len(A)
        '''
        # brute force O(N^2), timeout
        best = float("-inf")
        # can be optimize, only start from: zero & next index of negative values 
        for i in range(length):
            curr=0
            for j in range(i, length+i):
                curr = max(curr, 0)+A[j%length]
                best = max(curr, best)

        return best                
        '''

        # O(N)
        bestMax = float("-inf")
        curr=0
        # for normal case
        for i in range(length):
            curr = max(curr, 0)+A[i]
            bestMax = max(curr, bestMax)

        bestMin = float("inf")
        # for circular case, remove the min-sum subarray
        curr=0
        for i in range(length):
            curr = min(curr, 0)+A[i]
            bestMin = min(curr, bestMin)
        print(bestMax, bestMin)
        # for all negative case
        return bestMax if (sum(A)-bestMin)==0 else max(bestMax, sum(A)-bestMin)        