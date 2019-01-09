class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if not s or not wordDict:
            return False

        length = len(s)

        # recursive version with memorization. O(M*N^2)->O(M*N), M:dict size; N length of 's'
        mem = {}
        def helper(remain):
            if not remain: 
                return True

            if remain in mem:
                return mem[remain]
            
            result = False
            for w in wordDict:
                if remain.startswith(w):
                    temp = helper(remain[len(w):])
                    mem[remain[len(w):]] = temp
                    result |= temp

            return result
            
        return helper(s) 

        '''

        # DP O(M*N), with memory optimized, 30% (unbounded knapsack problem)
        dp = [False]*(length+1)
        dp[0] = True
        for i in range(1, length+1):

            for w in wordDict:
                ll = len(w)
                if ll <= i and s[i-ll:].startswith(w):
                    dp[i] |= dp[i-ll]

        return dp[-1]
        '''
