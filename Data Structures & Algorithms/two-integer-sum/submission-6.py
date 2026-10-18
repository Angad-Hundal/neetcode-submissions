class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make hash from value -> index
        # iterate all the nums
        # if diff = target - num in hash
        # return the two indexes
        # otherwise add the num in hash

        hash = {}


        for idx, num in enumerate(nums):
            diff = target - num

            if diff in hash:
                return [hash[diff], idx]
            
            hash[num] = idx
        