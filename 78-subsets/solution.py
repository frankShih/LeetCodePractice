class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result=[]
        if not nums:
            return result

        length = len(nums)
        '''
        # DFS, 36%
        def helper(ind, coms):
            result.append(coms)
            
            for i in range(ind, length):
                helper(i+1, coms+[nums[i]])
    
        helper(0, [])
        '''

        # BFS, 21%
        taskQ = [[0, []]]
        while taskQ:
            ind, sub = taskQ.pop(0)
            reult.append(sub)
            for i in range(ind+1, length):
                taskQ.append(i, sub+[nums[i]])

        return result
