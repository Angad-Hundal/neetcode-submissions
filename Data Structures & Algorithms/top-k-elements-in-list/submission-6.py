class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # make a hash from value -> count
        # make a nested array 
        # where array[i] shows the e which appear i times
        # thn start from back and tale first k elements

        count = {}

        freq = []
        for i in range(len(nums) + 1):
            # if len(nums) then if one element appear n times where willw e put it
            # so we need to have te freq array of length len(nums)
            freq.append([])
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # now we have all the count from value to count

        for value, times in count.items():
            freq[times].append(value)
        
        # now we have all the freq

        res = []

        for i in range(len(freq) -1 , 0 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


        