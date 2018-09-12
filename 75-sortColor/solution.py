class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        # 80% two-run, naive solution
        counter = [0]*3
        
        for n in nums:
            counter[n]+=1
        
        ind=0
        for i in range(len(counter)):
            for j in range(counter[i]):
                nums[ind]=i
                ind+=1
            
        
        # return nums    
        '''
        # 30%
        left, right, ind = -1, len(nums), 0
        while(ind<right):
            if nums[ind]==0:
                left+=1
                temp=nums[left]
                nums[left]=nums[ind]
                nums[ind]=temp
                if left==ind: ind+=1                
            elif nums[ind]==1:
                ind+=1                
            else:
                right-=1
                temp=nums[right]
                nums[right]=nums[ind]
                nums[ind]=temp

        # 60%
        left, right = 0, len(nums)-1
        for i in range(len(nums)):
            while(nums[i]==2 and i<right):
                temp = nums[right]
                nums[right] = nums[i]
                nums[i] = temp
                right-=1
            while(nums[i]==0 and i>left):
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                left+=1

            