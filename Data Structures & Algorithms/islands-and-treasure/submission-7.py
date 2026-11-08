class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid:
            return None

        def bfs():

            possible = [(1,0), (-1,0), (0,1), (0,-1)]
            rows, cols = len(grid), len(grid[0])
            queue = deque()
            visit = set()


            def addRoom(r,c):

                if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or grid[r][c] == -1:
                    return
                
                visit.add((r,c))
                queue.append((r,c))

                grid[r][c] = dist


            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 0:
                        queue.append((r,c))
                        visit.add((r,c))

            dist = 0
            while queue:

                for _ in range(len(queue)):
                    pop_r, pop_c = queue.popleft()
                    grid[pop_r][pop_c] = dist

                    for pr, pc in possible:
                        new_r, new_c = pop_r+pr, pop_c+pc
                        addRoom(new_r, new_c)
                
                dist += 1

        bfs()
