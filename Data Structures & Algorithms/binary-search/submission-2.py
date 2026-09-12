class Solution:
    # find the center index
    # if the target > index num
    # target in right
    # else -> target in left
    # find new target 
    # and keep on doing same thing 
    # untill new target same as old one 
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            idx = (right+left)//2

            if target == nums[idx]:
                return idx
            elif target > nums[idx]:
                left = idx + 1
            else:
                right = idx - 1
        
        return -1

        