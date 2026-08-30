class Solution:

    # make three dict
    # one for row, key as row
    # one for col, key as col
    # one for square, key as (r, c)
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for row_i in range(9):
            for col_i in range(9):
                if board[row_i][col_i] == ".":
                    continue
                elif (board[row_i][col_i] in rows) or (board[row_i][col_i] in cols) or (board[row_i][col_i] in square[(row_i//3, col_i//3)]):
                    return False
                cols[col_i].add(board[row_i][col_i])
                rows[row_i].add(board[row_i][col_i])
                square[(row_i//3, col_i//3)].add((board[row_i][col_i]))
        
        return True