class Solution(object):

    temp = {1:1, 2:2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        # pure math, 35%
        p = (1+math.sqrt(5))/2.
        q = (1-math.sqrt(5))/2.
        return int( (p**(n+1) - q**(n+1)) / (p-q) )

        # Dynamic programming: use the result from previous rounds

        # DP 1, 66%
        if n in Solution.temp:
            return Solution.temp[n]
        else:
            result = Solution.temp.get(n-1, self.climbStairs(n-1)) + Solution.temp.get(n-2, self.climbStairs(n-2))
            Solution.temp[n] = result

        return result
        '''

        # DP 2, 66%
        if not n: return n

        prv_1, prv_2 = 1, 0
        for i in range(n):
            prv_1, prv_2 = prv_1 + prv_2, prv_1

        return prv_1

