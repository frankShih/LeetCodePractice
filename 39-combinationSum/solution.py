class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result=[]
        if not target or not candidates:
            return result

        length = len(candidates)
        
        # DFS, 37%
        def helper(ind, coms):
            curSum = sum(coms)
            if curSum==target:
                result.append(coms)
                return
            elif curSum>target:
                return

            for i in range(ind, length): 
                helper(i, coms+[candidates[i]])
    
        helper(0, [])

        # DFS with early return, 66%
        candidates = sorted(candidates)

        def helper(ind, coms):
            curSum = sum(coms)
            if curSum==target:
                result.append(coms)
                return

            for i in range(ind, length): 
                if curSum+candidates[i]>target:
                    break
                helper(i, coms+[candidates[i]])
    
        helper(0, [])

        return result