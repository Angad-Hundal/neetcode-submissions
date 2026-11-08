class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        pacific = set()
        atlantic = set()

        # run a dfs from a location to pacific and atlantic
        # when all done
        # find the common ones and add it in result
        # return result
        rows, cols = len(heights), len(heights[0])
        possible = [(1,0), (-1,0), (0,1), (0,-1)]


        def dfs(r,c,ocean,prev_height):
            # if height more than prev height
            # then dont continue
            # because water cannot flow
            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in ocean or heights[r][c]<prev_height):
                return 
            
            ocean.add((r,c))

            for pr, pc in possible:
                dfs(pr+r, pc+c, ocean, heights[r][c])
        

        # iterate the first row and add it to pacific
        # iterate first col and add it to pacicif

        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])

        
        # iterate the last row and add it to atlantic
        # iterate the last col and add it to atlantics

        for col in range(cols):
            dfs(rows-1, col, atlantic, heights[rows-1][col])
        for row in range(rows):
            dfs(row, cols-1, atlantic, heights[row][cols-1])
        
        return list(pacific & atlantic)
            