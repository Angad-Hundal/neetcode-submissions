class Solution:

    # make a dict with the value and its all_count_list
    # sort the all_count_list
    # find top k
    # and get the values associated with them 


    def make_dict(self, nums: List[int]) -> dict:
        res = {}

        for num in nums:
            if not num in res:
                res[num] = 1
            else:
                res[num] += 1
            
        return res


    def make_res(self, count_array: list, k: int, val_to_count_dict: dict) -> list:
        count_array.sort(reverse=True)
        k_to_ckeck = set(count_array[:k])

        res = []

        for val, count in val_to_count_dict.items():
            if count in k_to_ckeck:
                res.append(val)
        
        return res


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) <= k:
            return nums
        
        # value -> all_count_list
        val_to_count_dict = self.make_dict(nums)

        all_count_list = list(val_to_count_dict.values())

        return self.make_res(all_count_list, k, val_to_count_dict)
        


        