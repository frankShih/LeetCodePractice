class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if not A:
            return 0
'''
        # DP solution O(N^2)
        d = {a:i for i, a in enumerate(A)}

        dp = [[2 for _ in range(len(A))] for _ in range(len(A))]
        # dp[i][j] - longest fibonacci from ind(i) to ind(j)
        ret = 0
        for j in range(len(A)):
            for k in range(j+1, len(A)):
                missing = A[k]-A[j]
                # must satisfy:
                #  1. missing < j < k
                #  2. missing in seq A
                if missing >= A[j]:
                    break
                if missing in d:
                    dp[j][k] = dp[d[missing]][j]+1
                    ret = max(dp[j][k], ret)
        return ret
'''

        # brute force solution O(N^2+log(M))
        S = set(A)
        ans = 0
        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                x, y = A[j], A[i] + A[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)

        return ans if ans >= 3 else 0