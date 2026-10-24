class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        pivot = left

        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                # middle greater than right
                # pivot in right hand side
                left = mid + 1
            else:
                # mid less than right
                right = mid
        pivot = left


        def binary_serach(left, right):
            while left <= right:
                mid = (left+right)//2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1
        
        res = binary_serach(0, pivot - 1)
        
        if res != -1:
            return res
        else:
            return binary_serach(pivot, len(nums) - 1)




        