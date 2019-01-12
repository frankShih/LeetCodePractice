class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        '''

        dpMax = nums[:]
        dpMin = nums[:]
        for i in range(1, length):
            currMin = dpMin[i-1]*nums[i]
            currMax = dpMax[i-1]*nums[i]
            dpMin[i] = min(currMax, currMin, dpMin[i])
            dpMax[i] = max(currMax, currMin, dpMax[i])

        print(dpMax, dpMin)
        return max(dpMax)

        # brute force time:O(N^2), 1%
        best = float("-inf")
        for i in range(length):
            temp=1
            for j in range(i, length):
                temp*=nums[j]
                if temp>best:
                    best=temp

        return best  
        '''  
        
        p = 1
        c_max = float('-inf')
        # deal with zero situation
        for n in nums:
            p*=n
            c_max = max(c_max, p)
            if n==0: p=1
        p = 1
        # reversed pass for odd-number negative value situaiton
        for n in nums[::-1]:
            p*=n
            c_max = max(c_max, p)
            if n==0: p=1
        
        return c_max