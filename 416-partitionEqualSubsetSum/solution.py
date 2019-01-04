class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        length = len(nums)
        target = sum(nums)
        
        if target%2:
            return False
        
        target/=2
        nums = sorted(nums)
        '''
        # O(n^2), timeout solution
        taskQ = [[nums[0], 0]]

        while taskQ:
            curr, ind = taskQ.pop()

            if curr==target:
                return True
            elif curr>target or ind==length-1:
                continue
            else:
                taskQ.append([curr+nums[ind+1], ind+1])
                taskQ.append([nums[ind+1], ind+1])

        return False
        '''
        
        # DP, 30% (mimic 0/1 knapsack problem)
        dp = [False]*(target+1)
        dp[0]=True

        for i in range(length):
            #each number can be chosen once
            for j in range(target, nums[i]-1, -1):
                # print(target, nums[i], j)
                dp[j]|=dp[j-nums[i]]
        # print(dp)

        return dp[-1]

