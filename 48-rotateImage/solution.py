class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix or not matrix[0]:
            return 
        
        '''
        # space O(N^2)
        record = dict()
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):
                record[(i, j)]=matrix[i][j]
                
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):        
                matrix[j][len(matrix[0])-i-1]=record[(i, j)]


        # space: O(N^2)
        length = len(matrix[0])
        for i in range(length):
            for j in range(length-1, -1, -1):   
                print(j, i)
                matrix[i].append(matrix[j][i])
        
        for i in range(length):
            for j in range(length):        
                matrix[i].pop(0)
        '''       
        # two options: 
        # 1. column reverse -> diagnal swap
        # 2. diagnal swap -> row reverse

        for i in range(len(matrix)):
            # diagnal-swap
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            rew.reverse()
            