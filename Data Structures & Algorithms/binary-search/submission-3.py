class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_idx = (left+right)//2
            mid = nums[mid_idx]

            if mid == target:
                return mid_idx
            elif target < mid:
                right = mid_idx - 1
            elif target > mid:
                left = mid_idx + 1
        
        return -1