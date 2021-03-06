class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        if len(pairs)<2:
            return 1

        # memory optimized version of gredduy solution
        # keep the end value & counter
        cur, res = float('-inf'), 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]: cur, res = p[1], res + 1
        return res

        '''
        # greedy, 32%
        pairs = sorted(pairs ,key=lambda l:l[1])
        path = []

        for p in pairs:
            if not path:
                path.append(p)
            elif path[-1][1]<p[0]:
                # since "pairs" is sorted by its end value,
                # the first one satisfying this condition is the best
                path.append(p)
        # print(visit)
        return len(path)

        # DP solution
        pairs = sorted(pairs ,key=lambda l:l[0])
        # print(pairs)
        length = len(pairs)
        dp=[1]*(length+1)

        for i in range(1, length):
            for j in range(i):
                if pairs[j][1]<pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
        '''
