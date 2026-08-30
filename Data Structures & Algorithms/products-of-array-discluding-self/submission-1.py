class Solution:

    # [1,2,3]
    # a single product of all = p
    # for all number is array: p//number

    # [1,2,0,3]
    # output: [0,0,6,0]

    # [1,2,0,3,0]
    # [all zeros]
    # product all zeros

    # make a var with the final product but without the zero
    # when dividing, do not divide by 0, instead use the product 

    def final_product(self, nums: List[int]) -> int:
        final = 1
        for num in nums:
            if num != 0:
                final = final*num
        return final
    
    def make_product_array(self, product: int, nums:list[int], has_zero: bool) -> list[int]:

        final = []
        for num in nums:
            if num != 0 and not has_zero:
                final.append(product//num)
            elif (num!=0 and has_zero):
                final.append(0)
            else:
                final.append(product)
        return final

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return [nums[0]]

        has_zero = False
        zero_count = nums.count(0)
        
        if zero_count > 1:
            return [0]*len(nums)
        elif zero_count == 1:
            has_zero = True
        
        final_num = self.final_product(nums)

        final_array = self.make_product_array(final_num, nums, has_zero)

        return final_array
        