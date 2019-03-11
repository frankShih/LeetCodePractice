class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        xy=yz=zx=0
        nrow, ncol = len(grid), len(grid[0])

        for i in range(nrow):
            temp= 0
            for j in range(ncol):
                if grid[i][j]:
                    xy+=1
                if grid[i][j]>temp:
                    temp =grid[i][j]

            zx+=temp

        for i in range(ncol):
            temp= 0
            for j in range(nrow):
                if grid[j][i]>temp:
                    temp =grid[j][i]

            yz+=temp

        print(xy, yz, zx)
        return xy+yz+zx
