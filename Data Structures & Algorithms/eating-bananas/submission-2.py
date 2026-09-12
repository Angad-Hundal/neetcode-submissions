class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            middle = (left + right) // 2
            
            time = 0
            for pile in piles:
                time += math.ceil(pile/middle)

                if time > h:
                    # dont need to continue
                    break
            
            if time <= h and res > middle:
                res = middle 
            
            # split the list now
            # time taken by k is less h
            # then consider k values in right hand side
            # if time taken by k is more than h
            # consider the k values in left hand side

            if time > h:
                right -= 1
            
            elif time < h:
                left += 1
        
        return res









        