class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # Time Limit Exceeded solution
        '''
        result=set()
        if not nums:
            return list(result)
        
        taskQ=[[nums, []]]
        while taskQ:
            remain, perm = taskQ.pop(0)
            if not remain:
                result.add(tuple(perm))
            for i in range(len(remain)):
                taskQ.append([remain[:i]+remain[i+1:], perm+[remain[i]]])

        return [list(x) for x in result ] 
        '''

        
        # DFS 64%
        result=[]
        if not nums:
            return result
        
        visit=set()
        length = len(nums)
        nums = sorted(nums)     # sort it first

        def helper(visit, perms):
            # print(remain, perms)
            if len(visit)==length:
                result.append(perms)
                return
            
            temp = None
            
            for i in range(length): 
                # skip same value in each round traversal
                if not(i in visit) and nums[i]!=temp:
                    temp=nums[i]
                    visit.add(i)
                    helper(visit, perms+[nums[i]])
                    visit.remove(i)
    
        helper(visit, [])
        return result