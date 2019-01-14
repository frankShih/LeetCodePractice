class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or not matrix[0]:
            return False

        nrow, ncol = len(matrix), len(matrix[0])
        
        '''
        # time: O(N*log(N))
        result=False
        
        def bSearch(left, right, array):
            while left<=right:
                m = left+(right-left)//2
                # print(m)
                if array[m]==target:
                    return True
                elif array[m]>target:
                    right=m-1
                else:
                    left=m+1

            return False        

        for i in range(nrow):
            if matrix[i][0]<=target<=matrix[i][-1]:
                # print("----------", i)
                result |= bSearch(0, ncol-1, matrix[i])

        return result        
        '''

        # O(N+M)
        i,j = nrow - 1, 0
        
        while i >= 0 and j < ncol:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
                
        return False
        