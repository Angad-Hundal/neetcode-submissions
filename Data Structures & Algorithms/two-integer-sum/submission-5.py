class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i and j
        # unique
        # hashmap
        # req -> seen
        
        # value -> index
        hash_map = {}

        for index, value in enumerate(nums):
            diff = target - value

            if diff in hash_map:
                return [hash_map[diff], index]
            
            hash_map[value] = index
