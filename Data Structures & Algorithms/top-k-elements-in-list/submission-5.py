class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # hash from value -> count
        count = {}

        # all nums appearing 1 appear at freq[1]
        # all nums appearing 2 appear at freq[2]
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # for all value we have their count
        
        for num, count in count.items():
            freq[count].append(num)
                

        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        