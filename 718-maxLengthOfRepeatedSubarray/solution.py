﻿class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0

        lenA, lenB = len(A), len(B)
        dp = [[0]*(lenA+1) for _ in range(lenB+1)]

        '''
        # sub-sequence version, can pass info to next row
        for i in range(1, lenB+1):
            for j in range(1, lenA+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if A[j-1]==B[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

        return dp[-1][-1]
        '''

        # sub-array version, have to check bestValue each row
        # dp[i][j] - longest common prefix of A[i:] & B[j:]
        result = 0
        for i in range(1, lenB+1):
            for j in range(1, lenA+1):
                if A[j-1]==B[i-1]:
                    dp[i][j] =dp[i-1][j-1]+1

                result = dp[i][j] if dp[i][j]>result else result
            # print(dp[i])

        return result

        # backward fashsion
        for i in range(lenA - 1, -1, -1):
            for j in range(lenB - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1]+1
        return max(max(row) for row in dp)
