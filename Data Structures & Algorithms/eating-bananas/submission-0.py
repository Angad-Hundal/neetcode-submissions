class Solution:
    # piles = [1,4,3,2]
    # num of bannans in 1st pile is 1 
    # num of b in 2nd pile is 4 etc
    # have 9 hours to eat all banannas
    # bannana per hour = k
    # each hour k bannanas
    # minimum k so all bannans eatten 

    # brute force solution
    # start from k=1 
    # and go untill k = max()
    # and for all calculate the hours
    # is hours cal > h
    # move to next k

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        for k in range(1, max(piles)+1):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)

                if time > h:
                    break
            
            if time <= h:
                return k





        