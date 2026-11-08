class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return None
        
        # replace every O with T
        # then change every T with X

        rows, cols = len(board), len(board[0])
        visit = set()
        possible = [(1,0), (-1,0), (0,-1), (0,1)]


        def dfs(r,c):
            if (r<0 or c<0 or r>=rows or c>=cols or board[r][c]!="O" or (r,c) in visit):
                return
            
            visit.add((r,c))

            board[r][c] = "T"
            
            for pr, pc in possible:
                dfs(pr+r, pc+c)
            
            
        # mark all boder O as T
        # run a dfs and mark all the places
        # connected with border O as T
        # these should not be converted to X
        # because they do not form surrounding
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and ((r in [0, rows-1]) or (c in [0, cols-1])) :
                    dfs(r,c)


        # convert the remaining O to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Convert T back to O
        # since T was temporary
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        




        