class Solution:
    '''
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        if not matrix or not matrix[0]:
            return ans
        #data = [[None]*5]*5 -> create references to the same list

        
        self.nRow = len(matrix)
        self.nCol = len(matrix[0])
        self.matrix = matrix
        
        pVisit = [[False]*self.nCol for _ in range(self.nRow)]        
        aVisit = [[False]*self.nCol for _ in range(self.nRow)]        
        
        for r in range(self.nRow):  # start from edges
            self.dfs(r, 0, pVisit)
            self.dfs(r, self.nCol-1, aVisit)
        
        for c in range(self.nCol):  # start from edges
            self.dfs(0, c, pVisit)
            self.dfs(self.nRow-1, c, aVisit)
            
        for r in range(self.nRow):
            for c in range(self.nCol):
                if pVisit[r][c] and aVisit[r][c]:
                    ans += [[r,c]]
        return ans
            
        
    def dfs(self, row, col, visit):
        if visit[row][col]: return
            
        visit[row][col] = True    
        
        for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r_temp, c_temp = row+dr, col+dc
            if 0 <= r_temp < self.nRow and \
            0 <= c_temp < self.nCol and \
            self.matrix[row][col] <= self.matrix[r_temp][c_temp]:
                self.dfs(r_temp, c_temp, visit)
    '''
    
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        if not matrix or not matrix[0]:
            return ans
        
        self.nRow, self.nCol = len(matrix), len(matrix[0])
        self.matrix = matrix
        
        pacific_reachable = set([(r,0) for r in range(self.nRow)]+[(0,c) for c in range(self.nCol)])
        atlantic_reachable = set([(r,self.nCol-1) for r in range(self.nRow)]+[(self.nRow-1, c) for c in range(self.nCol)])
        
        return list(self.bfs(pacific_reachable) & self.bfs(atlantic_reachable))
        
    def bfs(self, reachable_set: set) -> set:
        stack = list(reachable_set)
        
        while stack:
            (r, c) = stack.pop()
            for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r_temp, c_temp = r+dr, c+dc
                if 0 <= r_temp < self.nRow and 0 <= c_temp < self.nCol and (r_temp, c_temp) not in reachable_set and self.matrix[r][c] <= self.matrix[r_temp][c_temp]:
                    stack.append((r_temp, c_temp))
                    reachable_set.add((r_temp, c_temp))
        return reachable_set
                