class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # naive solution 99%
        length = len(nums)
        total = sum(nums)

        actual = (length+0)*(length+1)/2

        return actual-total
        '''

        # bitwise solution 50%
        result = 0
        for ind, val in enumerate(nums):
            result=result^ind^val
        return result