class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_without0 = 1
        zero = False
        zero_count = 0

        for num in nums:
            if num != 0:
                total_without0 *= num
            else:
                zero = True
                zero_count += 1

        
        res = []

        for num in nums:
            # num not zero but there is 0 somewhere in array
            if num != 0 and zero:
                res.append(0)
            # num is zero and there are more than 1 zeros
            elif num == 0 and zero_count > 1:
                res.append(0)
            # num is 0 and there is only 1 zero in the array
            elif num == 0 and zero_count == 1:
                res.append(total_without0)
            else:
                res.append(total_without0 // num)
        
        return res

                


        