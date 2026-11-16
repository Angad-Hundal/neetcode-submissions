"""
Approach: Recursion

Generate all possible subsets by considering one number at a time.

For each number, we have two choices:
1. Include the number in the subset.
2. Exclude the number from the subset.

Always pick the first number and recursively find all subsets of the remaining numbers.

Once recursion returns the subsets of the remaining numbers:
- Create subsets that include the current number by appending it to each existing subset.
- Keep the original subsets as they are to represent subsets that exclude the current number.

Combine both groups to get all possible subsets.

Base Cases:
- If the array is empty, return [[]] because an empty array has exactly one subset: the empty subset.
- If the array has one element, return [[], [num]] because we can either include or exclude that element.

The recursion solves the smaller problem first and builds the answer while returning, ensuring every subset is generated exactly once.

Time Complexity: O(n * 2^n)
Space Complexity: O(n * 2^n) including the output.
"""

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
