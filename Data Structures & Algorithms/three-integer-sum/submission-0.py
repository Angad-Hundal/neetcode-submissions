class Solution:
    # sort the nums
    # run a for loop on nums
    # fix the num
    # then have two idnexes
    # right and left index
    # if the sum larger than 0 then move left -= 1
    # if sum less than 0 then move right += 1
    # if equal: return the idexes
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # O(nlogn)
        result = []

        for idx, num in enumerate(nums):
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                if num + nums[left] + nums[right] == 0:
                    result.append([num, nums[left], nums[right]])
                    break
                elif num + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return result
        