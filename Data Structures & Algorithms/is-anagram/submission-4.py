class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def build_dict(e):
            result = {}

            for char in e:
                if char in result:
                    result[char] += 1
                else:
                    result[char] = 1
            return result
        
        s_res = build_dict(s)
        t_res = build_dict(t)

        return s_res == t_res
