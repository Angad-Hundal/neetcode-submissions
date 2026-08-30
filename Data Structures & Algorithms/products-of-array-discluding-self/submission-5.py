class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # make three arrays
        # prefix, suffix and final
        # prefix:
        # from o to len(nums)
        # [3,4,5]= [1,3,12]
        # Suffix:
        # [3,4,5] = [20,5,1]
        # final = prefix[i] * suffix[i]

        length = len(nums)
        prefix = [0]*length
        suffix = [0]*length
        final = [0]*length

        prefix[0] = 1
        for i in range(1, length):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix[length-1] = 1
        for i in range(length-2,-1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(len(final)):
            final[i] = prefix[i] * suffix[i]
        
        return final
        