class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        
        for idx, char in enumerate(s):
            seen = {char}
            current = 1
            for char in s[idx + 1: ]:
                if char in seen:
                    break
                else:
                    seen.add(char)
                current += 1
            if current > m:
                m = current
        
        return m 
                