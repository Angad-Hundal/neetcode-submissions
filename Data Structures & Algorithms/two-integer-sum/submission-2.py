class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for an index i in list
        # check all indexes from i to len(nums)
        # if target - value at i in those index then return those indexes

        for index, num in enumerate(nums):
            residual = target - num
            if residual in nums[index: len(nums)]:
                return [index, nums[index: len(nums)].index(target-num)]



                

        