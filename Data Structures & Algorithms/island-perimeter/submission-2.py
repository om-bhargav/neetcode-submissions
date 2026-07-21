class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dx = [0,1,-1,0]
        dy = [1,0,0,-1]
        def calcBoundaries(x,y):
            boundaries = 0
            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]
                if(cx < 0 or cy < 0 or cx >= m or cy >= n or grid[cx][cy] == 0):
                    boundaries += 1
            return boundaries
        ans = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]):
                    ans += calcBoundaries(i,j)
        return ans