class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we will use bfs


        if not grid:
            return None

        rows, cols = len(grid), len(grid[0])

        q = deque()
        visit = set()


        def addRoom(r,c):

            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or grid[r][c] == -1):
                return
            
            visit.add((r,c))
            q.append((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        dist = 0

        while q:
            # for all the nodes at that breadth level
            for i in range(len(q)):
                node_r, node_c = q.popleft()

                grid[node_r][node_c] = dist

                addRoom(node_r+1,node_c)
                addRoom(node_r-1,node_c)
                addRoom(node_r,node_c+1)
                addRoom(node_r,node_c-1)
            
            dist += 1

        