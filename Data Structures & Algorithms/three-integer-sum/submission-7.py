class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # for loop on nums
        # for index i
        # left = i+1
        # right = last
        # then do two sum

        nums.sort()

        result = []

        for idx, num in enumerate(nums):
            
            # handle duplicates for first index
            if idx >0  and nums[idx] == nums[idx-1]:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                total = num + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # handle duplicates for second and third index
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return result