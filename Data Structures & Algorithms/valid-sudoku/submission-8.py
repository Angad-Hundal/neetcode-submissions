class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create three hashes
        # one for each row
        # one for each col
        # and one for each sub box (row/3, col/3)

        rows_len, cols_len = len(board), len(board[0])

        rows = {} # row -> set()
        cols = {} # col -> set()
        boxes = {} # (row, col) -> set()


        for row in range(rows_len):
            for col in range(cols_len):

                if board[row][col] == ".":
                    continue

                value = board[row][col]

                if (value in rows.get(row, set())) or (value in cols.get(col, set())) or (value in boxes.get((row//3, col//3), set())):
                    return False

                if row in rows:
                    rows[row].add(value)
                else:
                    rows[row] = set(value)
                
                # for col
                if col in cols:
                    cols[col].add(value)
                else:
                    cols[col] = set(value)

                # for boxes
                if (row//3, col//3) in boxes:
                    boxes[(row//3, col//3)].add(value)
                else:
                    boxes[(row//3, col//3)] = set(value)
                
        
        return True







                