class Solution:
    def convert_to_set(self, string_to_convert):
        string_set = {}
        for char in string_to_convert:
            if char in string_set:
                string_set[char] +=1 
            else:
                string_set[char] = 1
        return string_set

    def isAnagram(self, s: str, t: str) -> bool:
        set_1 = self.convert_to_set(s)
        set_2 = self.convert_to_set(t)

        return set_1 == set_2