class Solution:


    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # convert the list into set
        # make an empty list 
        # for each number in the list (target - number) in set
        # then return both the index
        
        set_nums = set(nums)

        for index, num in enumerate(nums):
            if num in set_nums:
                return [index, nums.index(target-num)]

        