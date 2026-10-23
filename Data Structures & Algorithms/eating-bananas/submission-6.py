class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def complete(value, piles, h) -> bool:
            time = 0
            for pile in piles:
                time += math.ceil(pile/value)
            
            return time


        left = 1
        right = max(piles)
        res = max(piles)


        while left <= right:
            mid = (left+right)//2
            time = complete(mid, piles, h)

            if time <= h and mid < res:
                res = mid

            if time > h:
                left = mid + 1
            elif time < h:
                right = mid - 1
        
        return res
            
                
            




        

        