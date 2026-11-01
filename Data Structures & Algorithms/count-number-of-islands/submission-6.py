class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        count = 0
        allowed = [(1,0), (-1,0), (0,1), (0,-1)]
        rows = len(grid)
        cols  = len(grid[0])


        def dfs(row, col):

            if row>=rows or col>=cols or row<0 or col<0 or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            for r, c in allowed:
                new_r = row+r
                new_c = col+c

                dfs(new_r, new_c)

        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)


        return count
        