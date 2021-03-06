class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A)<3:
            return 0
        # naive solution, 10%
        records = []

        counter=1
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                counter+=1
            else:
                records.append(counter)
                counter=1

        records.append(counter)
        # print(records)

        result = 0
        for v in records:
            if v>1:
                result += ((v-1)+1)*(v-1)/2

        return result

        '''
        # dp solution
        dp = [0]*len(A)
        for i in range(2, len(A)):
            # each 3 make a 3-slice, length+1 == a new 3-slice & a length+1-slice
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1

        return sum(dp)
        '''
