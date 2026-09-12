class Solution:
    # find the center index
    # if the target > index num
    # update the index 
    # else 
    def search(self, nums: List[int], target: int) -> int:

        for idx, num in enumerate(nums):
            if num == target:
                return idx
        return -1
        