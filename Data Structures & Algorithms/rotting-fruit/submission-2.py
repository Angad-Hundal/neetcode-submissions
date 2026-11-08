class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        # we will use bfs here

        q = deque()
        visit = set()
        rows, cols = len(grid), len(grid[0])
        possible = [(1,0), (-1,0), (0,1), (0,-1)]

        fresh = 0

        for r in range(rows):
            for c in range(cols):
                # append rotten fruits to queue
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        

        def visitNode(r,c):
            # not grid[r][c] == 2
            # because we want to skip empty cells
            # and also the rotten fruits
            # so we add grid[r][c] != 1

            nonlocal fresh 
            if r<0 or c<0 or r>= rows or c>= cols or (r,c) in visit or grid[r][c] != 1:
                return 
            
            visit.add((r,c))
            # contaminate the fruit
            grid[r][c] = 2
            q.append((r,c))
            fresh -= 1


        minute = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                pop_r, pop_c = q.popleft()

                for r,c in possible:
                    visitNode(pop_r+r, pop_c+c)

            minute += 1
        
        # if any fresh left

        if fresh > 0:
            return -1
            
        return minute
        