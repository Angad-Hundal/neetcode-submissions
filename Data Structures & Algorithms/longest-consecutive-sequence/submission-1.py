class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()

        
        def possible(nums):
            res = []
            nums_set = set(nums)

            for num in nums:
                if not (num-1 in nums_set):
                    res.append(num)
            
            return res
        

        # now for all possible nums
        # run a while loop 
        # as long as num+1 in set
        # find length and have a max
        # calculate length

        possible = possible(nums)
        max_l = 0
        num_set = set(nums)

        for num in possible:
            length = 0
            while num in num_set:
                num += 1
                length += 1

            if length >= max_l:
                max_l = length
        
        return max_l


            

        