class NumArray(object):
    # Your NumArray object will be instantiated and called as such:
    # numArray = NumArray(nums)
    # numArray.sumRange(0, 1)
    # numArray.sumRange(1, 2)
    
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        '''
        self.dc = {-1:0}
        for i,v in enumerate(nums):
            self.dc[i] = self.dc[i-1] + v
        '''
        self.nums = nums
        (self.nums).insert(0, 0)
        
        for index in range(1, len(self.nums)):
            self.nums[index] += self.nums[index-1]
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        '''
        return self.dc[j]-self.dc[i-1]
        '''
        return self.nums[j+1]-self.nums[i]
        
        
        
