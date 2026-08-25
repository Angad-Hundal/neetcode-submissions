#

class Solution:

    def form_anagrams(self, strs: List[str]):
        # len(strs) > 1
        hash = {}

        for word in strs:
            sorted_list = sorted(word)
            sorted_word = "".join(sorted_list)
            if sorted_word in hash:
                # the array for this anagram already exists
                hash[sorted_word].append(word)
            else:
                # the array for this anagram dosent exist, encountering it first time
                hash[sorted_word] = [word]
        
        result = []
        for (_, value) in hash.items():
            result.append(value)
        
        return result

        
    # strs: array of strings
    # return: array of array of strings
    # Todo:
    # sort all strings
    # keep on putting them in hash
    # if the string already exists in hash
    # find the hash and add the string in that hash
    # else add the string into hash and make an array for it
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if (len(strs) == 0):
            return []
        elif len(strs) == 1:
            return [strs]
        
        else:
            return self.form_anagrams(strs)





        