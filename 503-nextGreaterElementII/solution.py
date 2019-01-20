class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        length = len(nums)
        indStack = []
        
        '''
        # duplicate array to mimic cyclic array O(N) , 40%
        result = [None]*(length*2)

        for i in range(length*2):
            while indStack and nums[indStack[-1]%length]<nums[i%length]:
                preInd = indStack.pop()
                result[preInd] = nums[i%length]

            indStack.append(i)    

        for i in range(length):
            if result[i]==None:
                result[i]=-1

        return result[:length]

        '''

        # more consice solution O(N), 67%
        ans = [-1] * length
        
        for i, n in enumerate(nums+nums):
            while stack and nums[indStack[-1]] < n:
                ans[indStack.pop()] = n
            indStack.append(i%len_nums)
        return ans


