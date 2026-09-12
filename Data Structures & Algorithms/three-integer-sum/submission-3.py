class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for idx, num in enumerate(nums):

            # same number again [0,1,1,1]
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                total = num + nums[left] + nums[right]

                if total == 0:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # appended one result
                    # to avoid duplicates 
                    # skip the same
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result