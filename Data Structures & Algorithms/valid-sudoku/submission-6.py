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
                value = board[row_i][col_i]
                if value == ".":
                    continue
                elif (value in rows) or (value in cols) or (value in square[(row_i//3, col_i//3)]):
                    return False
                cols[col_i].add(value)
                rows[row_i].add(value)
                square[(row_i//3, col_i//3)].add(value)
        
        return True