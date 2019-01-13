import sys

class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        length = len(A)
        if length<2:
            return 0

        # naive solution O(N*log(N))
        A = sorted(A)
        counter = 0
        for i in range(1, length):
            if A[i-1]>=A[i]:
                increase = A[i-1]-A[i]+1
                A[i]+=increase
                counter+=increase

        return counter
        