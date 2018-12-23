class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result=[]
        # if not nums:
        #     return result

        length = len(nums)
        nums = sorted(nums)
        
        # DFS, 33%
        def helper(ind, coms):
            result.append(coms)
            temp = None
            for i in range(ind, length):
                if temp!=nums[i]:
                    helper(i+1, coms+[nums[i]])
                temp=nums[i]
        
        helper(0, [])
        
        
        
        return result