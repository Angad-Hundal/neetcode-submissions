class Solution:

    def form_possible(self, nums: List[int], nums_set: set(int)) -> list[int]:
        possible = []

        for num in nums_set:
            if not (num-1 in nums_set):
                possible.append(num)
        
        return possible


    def longestConsecutive(self, nums: List[int]) -> int:
        # make a set of nums
        # iterate through the nums
        # if num -1 not in the set keep that for possible options
        # make a possible array 
        # then for each number in the possible array
        # run a while loop which will run 
        # for all untill the next number not in the array
        # and have a max variable for the final answer

        nums_set = set(nums)
        possible = self.form_possible(nums, nums_set)

        max_yet = 0

        for num in possible:
            length = 0
            while num in nums_set:
                num += 1
                length += 1
            
            if length > max_yet:
                max_yet = length 
        
        return max_yet



        
        