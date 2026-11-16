
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # let us try by recursion first
        # res = []
        # for every num in nums
        # find the subsets for nums - that num
        # and then append the subsets and [subset, num] into res

        def helper(nums):

            if not nums:
                return [[]]
            elif len(nums) == 1:
                return [[], nums]

            num = nums[0]
            rest_array = nums[1:]
            rest_subset = helper(rest_array)

            num_entry_subset = []

            for subset in rest_subset:
                num_entry_subset.append(subset + [num])
            
            num_entry_subset = num_entry_subset + rest_subset

            return num_entry_subset
            
        return helper(nums)
