class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        res = nums[0]

        while left <= right:

            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break
            
            mid = (left + right ) // 2

            if nums[mid] <= res:
                res = nums[mid]
            
            # if left < middle
            # move to left to mid + 1
            if nums[left] <= nums[mid]:
                left = mid + 1

            # else:
            # move right to mid -1
            else:
                right = mid - 1
            
        return res 

