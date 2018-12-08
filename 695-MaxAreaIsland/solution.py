class Solution:
    
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    # 20%
    '''
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        best = 0
        if not(grid) or not(grid[0]): return best
        
        visit = [ [0]*len(grid[0]) for _ in range(len(grid)) ]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result = self.helper(i, j, grid, visit)
                if result > best: best=result
                    
        return best
    
    def helper(self, x, y, grid, visit):
        # print("in", x, y)
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
            return 0
        
        if not(grid[x][y]): 
            visit[x][y] = 1
            return 0
        
        if visit[x][y]: 
            return 0
        
        dist=1
        visit[x][y] = 1
        for d in self.directions:
            # print("call", x+d[0], y+d[1])
            dist+=self.helper(x+d[0], y+d[1], grid, visit)
        
        return dist
    '''

    # 40%
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        best = 0
        if not(grid) or not(grid[0]): return best
        
        rowN , colN = len(grid), len(grid[0])
        
        def helper(x, y, grid):
            if x<0 or y<0 or x>=rowN or y>=colN or not(grid[x][y]):
                return 0

            dist=1
            grid[x][y] = 0
            dist+=helper(x+1, y, grid)
            dist+=helper(x, y+1, grid)
            dist+=helper(x-1, y, grid)
            dist+=helper(x, y-1, grid)
            return dist

    
        for i in range(rowN):
            for j in range(colN):
                result = helper(i, j, grid)
                if result > best: best=result
                    
        return best
    