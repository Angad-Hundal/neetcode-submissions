class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        max_area = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])


        def dfs(r,c):

            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == 0):
                return 0
            
            area = 1
            grid[r][c] = 0
            
            for dr, dc in directions:
                area += dfs(dr+r, c+dc)
            return area

            


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area


        