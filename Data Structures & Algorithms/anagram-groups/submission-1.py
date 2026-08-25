class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strs = [...]
        # sorted_strs = [...]
        # hashmap: sorted_string -> []
        # combine all the lists


        sorted_list = list()
        hashmap = {}

        for val in strs:
            sorted_word = "".join(sorted(val))
            sorted_list.append(sorted_word)
        
        for idx, val in enumerate(sorted_list):
            if val in hashmap:
                hashmap[val].append(strs[idx])
            else:
                hashmap[val] = [strs[idx]]
        
        final = []

        for values in hashmap.values():
            final.append(values)
        
        return final
