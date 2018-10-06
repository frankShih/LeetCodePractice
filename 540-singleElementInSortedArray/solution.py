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
            
            if nums[m]==nums[m+1]:
                l=m+2
        # 56%
        '''
            elif nums[m]==nums[m-1]:    #index out of range
                r=m
            else :
                return nums[m]
        '''
        # 100%
            else:
                r=m
        return nums[l]