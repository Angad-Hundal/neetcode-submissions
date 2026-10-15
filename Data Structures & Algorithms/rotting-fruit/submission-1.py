class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        

        # we will use bfs

        rows, cols = len(grid), len(grid[0])

        q = deque()
        visit = set()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        


        def addNode(r,c):
            nonlocal fresh

            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] != 1 or (r,c) in visit):
                return
            
            grid[r][c] = 2
            fresh -= 1
            q.append((r,c))
            visit.add((r,c))

        while q and fresh > 0:
            for _ in range(len(q)):
                er, ec = q.popleft()

                addNode(er + 1, ec)
                addNode(er - 1, ec)
                addNode(er, ec + 1)
                addNode(er, ec - 1)

            time += 1
        

        if fresh == 0:
            return time
        else:
            return -1




                

        