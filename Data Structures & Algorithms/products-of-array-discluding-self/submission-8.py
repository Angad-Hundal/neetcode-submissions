class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]

        # nums =   [1, 5, 10, 4]
        # prefix = [1, 1, 1*5, 5*10]

        for idx in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[idx-1])
    
        suffix = [1 for i in range(len(nums))]

        for idx in range(len(nums)-2, -1, -1):

            suffix[idx] = suffix[idx+1] * nums[idx+1]

        res = []


        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])
        
        return res


        