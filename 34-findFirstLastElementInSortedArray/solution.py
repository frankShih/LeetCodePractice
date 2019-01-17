class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)-1

    # O(N) 20%
        if not(len(nums)): return [-1, -1]
        '''
        while l<r and nums[l]!=nums[r]:
            if nums[l]<target: l+=1
            if nums[r]>target: r-=1
        
        return [l, r] if nums[l]==target else [-1, -1]
        '''

    # O(log(N)) 72%
        l = self.binarySearch(nums, target)
        r = self.binarySearch(nums, target+1)-1
        # print(l, r)
        if nums[-1]==target:    #target at last position
            return [l, r+1]
        elif nums[l]==target:
            return [l, r]    
        else:
            return [-1, -1]

    def binarySearch(self, nums, target):
        l, r = 0, len(nums)-1        
                
        while l<r:
            m=l+(r-l)//2
            if nums[m]<target: 
                l=m+1
            else:
                r=m        
        return l