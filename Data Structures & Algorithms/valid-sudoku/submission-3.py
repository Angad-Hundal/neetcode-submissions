class Solution:
    # have a list of sets
    # append all rows as a set in the list
    # append all columns as a set in the list
    # append the squares as a set in the list
    # then iterate over the sets in the list
    
    def check_rows(self, board: List[List[str]]) -> bool:

        for row in board:
            row_set = set()
            for number in row:
                if number != "." and number in row_set:
                    return False
                else:
                    row_set.add(number)
        return True


    def check_columns(self, board: List[List[str]]) -> bool:

        for i in range(0,9):
            column_set = set()
            for row in board:
                if row[i] != "." and row[i] in column_set:
                    return False
                else:
                    column_set.add(row[i])
        
        return True
    

    def check_square(self, board: List[List[str]]) -> bool:

        for start_row in [0,3,6]:
            for start_col in [0,3,6]:
                square_set = set()

                for i in range(start_row, start_row+3):
                    for j in range(start_col, start_col +3):
                        number = board[i][j]
                        if number!="." and number in square_set:
                            return False
                        else:
                            square_set.add(board[i][j])
        return True




    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_rows(board) or self.check_columns(board) or self.check_square(board)

