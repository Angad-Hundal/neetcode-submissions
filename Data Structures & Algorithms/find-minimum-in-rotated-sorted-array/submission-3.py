class Solution:
    # res = idx 0 
    # left = 0
    # right = last of list idx
    # find the middle

    # if middle greater than left
    # serach right

    # else 
    # search left
    def findMin(self, nums: List[int]) -> int:

        res = nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            middle = (left + right)//2

            if nums[middle] <= res:
                res = nums[middle]

            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return res

                
        
        