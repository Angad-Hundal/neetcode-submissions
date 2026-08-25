class Solution:

    def make_dict(self, word: str) -> dict[str, int]:
        # for all words make a dict

        final_dict = dict()

        for char in word:
            if char in final_dict:
                final_dict[char] += 1
            else:
                final_dict[char] = 1
        return final_dict



    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = self.make_dict(s)
        t_dict = self.make_dict(t)

        return s_dict==t_dict
        