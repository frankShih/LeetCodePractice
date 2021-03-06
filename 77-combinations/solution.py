class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        

        result=[]
        if not n:
            return result
        '''
        # DFS 37%
        def helper(ind, coms):
            # print(remain, perms)
            if len(coms)==k:
                result.append(coms)
                return
            
            for i in range(ind, n+1): 
                # skip same value in each round traversal
                helper(i+1, coms+[i])
    
        helper(1, [])
        return result

        # DFS, with back-tracking, 40%
        def helper(ind, coms):
            # print(remain, perms)
            if len(coms)==k:
                result.append(list(coms))
                return
            
            for i in range(ind, n+1): 
                # skip same value in each round traversal
                coms.add(i)
                helper(i+1, coms)
                coms.remove(i)
    
        helper(1, set())
        '''
