class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        if not grid:
            return None
        
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        possible = [(1,0), (-1,0), (0,-1), (0,1)]
        

        def dfs(r, c, distance):

            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == -1:
                return

            if grid[r][c] < distance:
                return
            
            grid[r][c] = distance


            for dr, dc in possible:
                dfs(r + dr, c + dc, distance + 1)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # start from inside outside
                    dfs(r, c, 0)
    
