class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # measure k
        left = 1
        right = max(piles)
        res = right # k value

        # iterate over k values
        while left <= right:
            middle = (left + right) // 2 # find the middle k value
            
            # find the overall time taken for that k
            time = 0
            for pile in piles:
                time += math.ceil(pile/middle) # ceil because we want upper limit

                # if time > h:
                #     # dont need to continue
                #     break
            
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









        