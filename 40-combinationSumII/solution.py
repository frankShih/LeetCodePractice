class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        if not target or not candidates:
            return result

        length = len(candidates)
        
        # DFS with early return, 85%
        candidates = sorted(candidates)

        def helper(ind, coms):
            curSum = sum(coms)
            if curSum==target:
                result.append(coms)
                return
            temp=None
            for i in range(ind, length): 
                if curSum+candidates[i]>target:
                    break
                if temp == candidates[i]:
                    continue
                temp = candidates[i]    
                helper(i+1, coms+[candidates[i]])
    
        helper(0, [])

        return result
