class Solution:
    # var max_area
    # iterate through heights 
    # for each height
    # calculate right most 
    # run a while loop till n and till height is not less than current hright
    # run a while loop for left most 
    # run a loop from i to 0 in reverse
    # til height not less than current 
    # calculate the area
    # and update max
    # return max
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for idx, height in enumerate(heights):

            right_most = idx
            while right_most < n and heights[right_most] >= height:
                right_most += 1
            right_most -= 1
            
            left_most = idx
            while left_most > 0 and heights[left_most] >= height:
                left_most -= 1
            left_most += 1
            
            area = height*(right_most - left_most + 1)
            max_area = max(max_area, area)

        
        return max_area
        