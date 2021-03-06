class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        if not n or n<2:
            return 0
        '''
        # timeout solution O(N!)
        taskQ =  [[1]*n]
        record = set()
        best = 1

        while taskQ:
            curr = taskQ.pop(0)
            if len(curr)<2 or tuple(curr) in record:
                continue
            record.add(tuple(curr))
            temp = 1
            for c in curr:
                temp*=c

            if temp>best:
                best=temp

            for i in range(1, len(curr)):
                taskQ.append(curr[:i-1]+[sum(curr[i-1:i+1])]+curr[i+1:])

            # print(taskQ)
        return best
        '''

        # DP, 40%
        dp = [0]*(n+1)
        dp[1]=1
        for i in range(2, n+1):

            for j in range(1, i//2+1):
                # compare current value with each possible split
                dp[i] = max(dp[i], max(j, dp[j]) * max(i-j, dp[i-j]))

        return dp[-1]

        # pure math: dp[i]=3*dp[i-3], for i>6