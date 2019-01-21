class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        length = len(nums)

        '''
        # forward checking O(N), 60%
        p = None
        for i in range(length-1):
            if nums[i] > nums[i+1]:
                if p is not None:
                    return False
                p = i
        # 1. no reverse occured
        # 2. reverse happened at start/end of array
        # 3. the values around still satisfied the condition
        #    (replace current/next value)
        return (p is None or \
                p == 0 or \
                p == len(nums)-2 or \
                nums[p-1] <= nums[p+1] or \
                nums[p] <= nums[p+2])
        '''

        # more readable O(N), 24%
        count = 0
        for i in range(1, length):
            if nums[i] < nums[i - 1]:
                count += 1
                # at least 2 values are affected by incoming num, so change it
                # otherwise (happened at the beginning), ignore it
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i-1] = nums[i]

        return count<=1
