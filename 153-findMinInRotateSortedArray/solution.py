class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 100%
        l, r = 0, len(nums)-1
        
        while l<r:
            m=l+(r-l)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
                
        return nums[l]        