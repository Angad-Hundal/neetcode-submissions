class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # rows, cols
        # run DFS
        # for all rows and cols
        # if the entry "1"
        # then run a dfs on that
        # for surrounding regions
        # mark them as "0"
        # and increase the count
        # if entry out of bound then return the dfs
        # run a dfs for all the surrouding regions

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        possible = [(1,0), (-1,0), (0,-1),(0,1)]

        def dfs(r,c):

            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == "0"):
                return

            grid[r][c] = "0"

            for row,col in possible:
                newr, newc = r+row, c+col
                dfs(newr, newc)

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)
        
        return count