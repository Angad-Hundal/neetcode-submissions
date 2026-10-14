class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        allowed = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0


        def bfs(r, c):
            q = deque()

            grid[r][c] = "0"
            q.append((r,c))

            while q:
                node_r, node_c = q.popleft()

                for dr, dc in allowed:
                    nr, nc = dr + node_r, dc + node_c

                    if (nr<0 or nc<0 or nr>=len(grid) or nc>= len(grid[0]) or grid[nr][nc] == "0"):
                        continue
                    
                    q.append((nr,nc))
                    grid[nr][nc] = "0"


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    bfs(row, col)
                    count += 1
        
        return count

        