class Solution:
    # right, left
    # up, down
    # run while loops
    # untill proper row and proper column found
    # start with row
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        target_row = 0
        up = 0
        down = len(matrix) - 1

        while up <= down:
            target_row = (up + down)//2


            # less than the first element in the row
            if matrix[target_row][0] > target:
                down = target_row - 1
            # greater than the last element in the row
            elif matrix[target_row][-1] < target:
                up = target_row + 1
            else: # 
                # we have found the target row
                break
        
        target_col = 0
        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            target_col = (right + left)//2
            if matrix[target_row][target_col] == target:
                return True
            elif matrix[target_row][target_col] > target:
                right = target_col - 1
            else:
                left = target_col + 1
        
        return False


        