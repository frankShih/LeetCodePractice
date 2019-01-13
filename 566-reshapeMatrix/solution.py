class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        # space O(R*C)
        result=[]
        if not nums or not r or not c:
            return result
        nrow, ncol = len(nums), len(nums[0])
        
        if nrow*ncol<r*c or nrow==r and ncol==c:
            return nums

        temp = []    
        for row in nums:
            temp.extend(row)

        result = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                result[i][j]=temp.pop(0)

        '''
        # more consice solution, space:O(C)
        for row in nums:
            for elem in row:
                temp.append(elem)
                if len(temp)==c:
                    result.append(temp)
                    temp=[]
        '''

        return result            
        