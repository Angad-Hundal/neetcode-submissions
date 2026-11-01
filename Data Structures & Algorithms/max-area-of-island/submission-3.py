class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        

        # we will use dfs
        # iterate on rows and cols
        # when the position is 1
        # run a dfs on possible directions
        # and keep area 
        # if area > max yet
        # then update it

        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        possible = [(1,0), (-1,0), (0,1), (0,-1)]


        def dfs(row, col, area):

            nonlocal max_area

            if row<0 or col<0 or row>=rows or col>=cols or grid[row][col] == 0:
                return
            
            grid[row][col] = 0
            max_area = max(max_area, area)

            for r, c in possible:
                dfs(r+row, c+col, area+1)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r,c,1)
        

        return max_area

