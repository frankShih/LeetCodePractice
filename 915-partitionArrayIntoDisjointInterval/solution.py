class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        length=len(A)
        '''
        # O(N*log(N)), using sortInd
        sortedInd = sorted(range(length), key=lambda x:A[x])

        maxInd = 0
        for i in range(length):
            if sortedInd[i]>maxInd:
                maxInd = sortedInd[i]
            if i ==maxInd:
                break

        print(maxInd)     
        return maxInd+1


        # DP O(N)
        maxleft = [None] * length
        minright = [None] * length

        m = A[0]
        for i in xrange(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in xrange(N-1, -1, -1):
            m = min(m, A[i])
            minright[i] = m

        for i in xrange(1, N):
            if maxleft[i-1] <= minright[i]:
                return i
        '''

        leftmax = currmax = A[0]
        p_idx = 0
        for i, a in enumerate(A):
            currmax = max(currmax, a)
            if leftmax > a:
                # update the split point, 
                # also the leftmax to currmax (leftMAX < rightMIN)
                p_idx = i
                leftmax = currmax

        return p_idx+1        