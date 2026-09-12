class Solution:
    # start the left and right index
    # res variable
    # while loop left < right
    # calucluate the area  
    # if area larger then update
    # whichever one smaller 
    # shift that index
    # both equal shift either 
    def maxArea(self, heights: List[int]) -> int:

        res = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            area = min(heights[left], heights[right])*(right - left)
            if area > res:
                res = area
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return res

        