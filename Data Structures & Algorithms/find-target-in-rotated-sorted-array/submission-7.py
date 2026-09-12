class Solution:

    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right )// 2

            if target == nums[middle]:
                return middle

            if nums[left] <= nums[middle]:
                # left is sorted

                if nums[left] <= target < nums[middle]:
                    right = middle -1
                else:
                    # search on right
                    # on the messed up side of array
                    left = middle + 1
            
            else:
                # right is sorted 
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    # on the messed up side of array
                    right = middle -1

        
        return -1
            
        

            