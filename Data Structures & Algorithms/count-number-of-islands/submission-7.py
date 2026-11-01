class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        count = 0
        allowed = [(1,0), (-1,0), (0,1), (0,-1)]
        rows = len(grid)
        cols  = len(grid[0])


        def bfs(r,c):
            q = deque([(r,c)])

            grid[r][c] = "0"

            while q:
                er, ec = q.popleft()

                for dr, dc in allowed:
                    nr = dr+er
                    nc= dc+ec

                    if nr<0 or nc<0 or nr>=rows or nc>= cols or grid[nr][nc] == "0":
                        continue
                    
                    q.append((nr,nc))
                    grid[nr][nc] = "0"

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    bfs(row, col)
        
        return count
        