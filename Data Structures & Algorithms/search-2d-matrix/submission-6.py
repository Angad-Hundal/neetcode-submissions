class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        def find_row(matrix: List[List[int]], target: int) -> int:
            up = 0
            down = len(matrix)

            while up <= down:
                mid_idx = (up+down)//2

                # if target more than the row last
                # then up = mid + 1
                # if target less than first element
                # down = mid -1
                if matrix[mid_idx][0] > target:
                    down = mid_idx - 1
                elif target > matrix[mid_idx][-1]:
                    up = mid_idx + 1
                else:
                    return mid_idx
        

        row = find_row(matrix, target)

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid_i = (left+right)//2

            if matrix[row][mid_i] == target:
                return True
            elif matrix[row][mid_i] > target:
                left = mid_i + 1
            else:
                right = mid_i - 1
        
        return False
