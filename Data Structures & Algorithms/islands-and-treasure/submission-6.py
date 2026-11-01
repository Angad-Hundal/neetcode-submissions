class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])

        def dfs(r, c, dist):
            # out of bounds or water
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == -1:
                return
            # already have a path that's as good or better
            # (skip this check for the starting treasure, dist == 0)
            if dist > grid[r][c]:
                return

            grid[r][c] = dist

            dfs(r + 1, c, dist + 1)
            dfs(r - 1, c, dist + 1)
            dfs(r, c + 1, dist + 1)
            dfs(r, c - 1, dist + 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    dfs(r, c, 0)