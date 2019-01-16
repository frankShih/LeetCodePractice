class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []

        # naive Solution 90%, O(N^2)
        result = [[None]*n for _ in range(n)]

        dirRow = [0, 1, 0, -1]
        dirCol = [1, 0, -1, 0]

        counter = 1
        currRow, currCol, currDir = 0, 0, 0
        while counter<n^2:
            result[currRow][currCol] =counter
            counter+=1
            if currRow+dirRow[currDir]>=n or currCol+dirCol[currDir]>=n or result[currRow+dirRow[currDir]][currCol+dirCol[currDir]]!=None:
                currDir = (currDir+1)%4

            currRow+=dirRow[currDir]
            currCol+=dirCol[currDir]

        return result