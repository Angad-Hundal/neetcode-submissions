class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        allowed = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= len(grid) or c >= len(grid[0]) or
                grid[r][c] == "0"):
                return

            grid[r][c] = "0"

            for dr, dc in allowed:
                dfs(r + dr, c + dc)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1

        return count