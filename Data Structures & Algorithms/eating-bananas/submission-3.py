class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            # k value we checking
            middle = (left + right) // 2
            
            time = 0
            for pile in piles:
                time += math.ceil(pile/middle)

            # if time <= h and middle < res:
            #     # found lower k value
            #     res = middle 
        
            if time > h:
                left = middle + 1
            
            elif time <= h:
                res = middle
                right = middle -1

        
        return res









        