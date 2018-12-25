class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        if len(nums)<2:
            return nums[0]
        
        '''
        # brute force, timeout
        cand=[]
        for i in range(len(nums)):
            temp = nums[i]
            cand.append(temp)

            for j in range(i+1, len(nums)):
                temp+=nums[j]
                cand.append(temp)

        return max(cand)
        '''
        
        '''
        
        dp = [None]*len(nums)
        dp[0]=nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        
        # print(dp)
        
        return max(dp)
        '''
        
        curr = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            curr = max(curr+nums[i], nums[i])
            best = max(best, curr)

        return best