class Solution:

    # [1,1,1,2,2,2,3,3,3] k=2

    # make a dict with num as the key and count as value
    # take the dict.values() and sort it
    # take first k items from that list and make a set
    # make final list = []
    # iterate the keys of the dict and if the value in set 
    # append it in that list

    def make_dict(self, nums: list[int]) -> dict[int, int]:

        final_dict = dict()

        for number in nums:
            if number in final_dict:
                final_dict[number] += 1
            else:
                final_dict[number] = 1

        return final_dict


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_dict = self.make_dict(nums)

        sorted_values = sorted(nums_dict.values(), reverse=True)[:k]

        top_k_set = set(sorted_values)

        final_list = []

        for key, value in nums_dict.items():
            if value in top_k_set:
                final_list.append(key)
    
        return final_list

        