class Solution:
    # make an array max_left
    # make an array max_right
    # iterate through the heights
    # and keep on storing max in the arrays 
    # two for loops

    # then iterate through each index
    # find the area by
    # min(left, right) - height
    def trap(self, height: List[int]) -> int:
        
        max_left = []
        max_right = []

        max_num = 0
        for idx, num in enumerate(height):
            max_left.append(max_num)

            if num > max_num:
                max_num = num
        
        max_num = 0
        for idx, num in enumerate(height[::-1]):
            max_right.append(max_num)

            if num> max_num:
                max_num = num
        max_right.reverse()
        
        area = 0
        for idx, h in enumerate(height):
            area += max(0, min(max_left[idx], max_right[idx]) - h)
        
        return area

        

