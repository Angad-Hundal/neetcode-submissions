class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = []
        max_yet = 0

        for h in height:
            max_left.append(max_yet)
            if h > max_yet:
                max_yet = h

        
        max_right = []
        max_yet = 0

        for h in height[::-1]:
            max_right.append(max_yet)
            if h > max_yet:
                max_yet = h
        
        res = 0

        for i,h in enumerate(height):
            hols = min(max_left[i], max_right[i]) - h
            res += hols

        return res



        