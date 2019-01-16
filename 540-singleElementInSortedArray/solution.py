class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, len(nums)-1
        while l<r:
            # print(l, r)
            m = l + (r-l)//2
            if m%2:
                m-=1
            # using index to determine wether the single is in left/right
            if nums[m]==nums[m+1]:
                l=m+2
            # 56%
            # elif nums[m]==nums[m-1]:    #index out of range
            #     r=m
            # else :
            #     return nums[m]
            else:
            # 100%
                r=m
        return nums[l]
        '''

        result=0
        for n in nums:
            result^=n

        return result
        '''
