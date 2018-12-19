class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result=[]
        if not nums:
            return result
        '''
        # DFS 15%
        def helper(remain, perms):
            # print(remain, perms)
            if not remain:
                result.append(perms)
                return
            for i in range(len(remain)):
                helper(remain[:i]+remain[i+1:], perms+[remain[i]])

        helper(nums, [])
        '''

        # BFS 30%
        taskQ=[[nums, []]]
        while taskQ:
            remain, perm = taskQ.pop(0)
            if not remain:
                result.append(perm)
            for i in range(len(remain)):
                taskQ.append([remain[:i]+remain[i+1:], perm+[remain[i]]])

        return result