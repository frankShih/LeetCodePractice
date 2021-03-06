class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        result = []

        if not matrix or not matrix[0]:
            return result

        nrow, ncol = len(matrix)    , len(matrix[0])
        '''
        seen = [[False] * ncol for _ in matrix]
        # clockwise direction: up -> right -> down -> left
        dirRow = [0, 1, 0, -1]
        dirCol = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(nrow * ncol):
            result.append(matrix[r][c])
            seen[r][c] = True
            currRow, currCol = r + dirRow[di], c + dirCol[di]
            if 0 <= currRow < nrow and 0 <= currCol < ncol and not seen[currRow][currCol]:
                # unvisited and in the bound
                r, c = currRow, currCol
            else:
                # change to next direction
                di = (di + 1) % 4
                r, c = r + dirRow[di], c + dirCol[di]
        return result
        '''

        while matrix:
            result+=matrix.pop(0)
            # print(matrix)
            # The single star * unpacks the sequence/collection into positional arguments
            # transpose operation
            matrix = list(zip(*matrix))[::-1]
            # print(matrix)

        return result      
