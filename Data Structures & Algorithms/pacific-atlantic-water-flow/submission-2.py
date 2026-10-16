class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return []
        
        pac, atl = set(), set()
        # visit = set()
        rows, cols = len(heights), len(heights[0])


        def dfs(r,c,visit, prev_height):

            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or heights[r][c] < prev_height):
                return

            visit.add((r,c))

            dfs(r+1,c,visit,heights[r][c])   
            dfs(r-1,c,visit,heights[r][c])     
            dfs(r,c+1,visit,heights[r][c])      
            dfs(r,c-1,visit,heights[r][c])       
        


        # for first and last row
        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows-1, col, atl, heights[rows-1][col])
        

        # for first and last col
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols-1, atl, heights[row][cols-1])

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        
        return result
        

        