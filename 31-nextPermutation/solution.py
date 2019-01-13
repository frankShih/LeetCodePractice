class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        length = len(nums)
        if length<2:
            return

        def reverseRange(i, j, arr):
            while i<j:
                swap(i, j, arr)
                i+=1
                j-=1
            
        def swap(i, j, arr):
            arr[i]+=arr[j]
            arr[j]=arr[i]-arr[j]
            arr[i]=arr[i]-arr[j]
        
        
        ind1 = -1    
        # backward check for first decreasing index
        for i in range(length-1, 0, -1):
            if nums[i]>nums[i-1]:
                ind1=i-1
                break
        
        if ind1>=0:
            # if break point found, forward finding the smallest value >nums[ind1]
            ind2 = ind1-1
            for i in range(ind1, length):
                if nums[i]>nums[ind1]:
                    ind2=i
                    # break
            
            swap(ind1, ind2, nums)
            # the rest part. reset it to increasing order
            reverseRange(ind1+1, length-1, nums)
        else:
            # all decreasing, reverse it
            reverseRange(0, length-1, nums)

            

