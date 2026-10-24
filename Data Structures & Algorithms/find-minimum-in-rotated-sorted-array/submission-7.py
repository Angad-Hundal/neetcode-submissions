class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            # increase (high) - > peak -> lowest -> increase (smaller)

            if nums[left] < nums[right]:
                # already sorted
                res = min(res, nums[left])
                break

            mid = (left+right)//2

            if nums[mid] <= res:
                res = nums[mid]

            if nums[left] <= nums[mid]:
                # find in right
                # left hand already sorted
                left = mid + 1
            
            else:
                # num[letf] > nums[mid]
                # find in mid to right
                right = mid - 1
        return res
            

            



        