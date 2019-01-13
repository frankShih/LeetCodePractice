class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        # two round traversal
        ind=[];
        zeros = [];
        for x in range(len(nums)):
            if nums[x]==0:
                ind.append(x)
                   
        for i in reversed(ind):
            del (nums[i])
            nums.append(0);
            
        '''

        # one round traversal

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
