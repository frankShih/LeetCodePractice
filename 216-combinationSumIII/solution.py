class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        result=[]
        if not k or not n:
            return result
        
        # DFS with early return, 61%

        def helper(ind, coms):
            curSum = sum(coms)
            if len(coms)==k:
                if curSum==n:
                    result.append(coms)
                return
            
            for i in range(ind, 10): 
                if curSum+i>n:
                    break

                helper(i+1, coms+[i])
    
        helper(1, [])

        return result
