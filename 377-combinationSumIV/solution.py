class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums:
            return 0

        '''
        # DP O(N*T), 80%
        dp = [0]*(target+1)    
        dp[0]=1
        for i in range(target+1):
            for num in nums:
                if i+num>target:
                    continue
                dp[i+num]+=dp[i]    

        return dp[-1]        
        '''

        # DFS with memorization, O(N*T)
        memo = {}
        def helper(remain, mem):
            if remain in mem:
                return mem[remain]
            if not remain:
                return 1

            result = 0
            for n in nums:
                if remain <n:
                    continue
                result+=helper(remain-n, mem)
            mem[remain] = result

        helper(target, memo)
        return memo[target]    
