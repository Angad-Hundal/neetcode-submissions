class Solution:
    # max variable
    # run a for loop
    # run another for loop
    # for each find the area
    # if area greater update the max var
    def maxArea(self, heights: List[int]) -> int:

        best = 0

        for left, height in enumerate(heights):

            for right in range(left+1, len(heights)):

                area = (right-left)* min(height, heights[right])
                if area > best:
                    best = area
        
        return best
        