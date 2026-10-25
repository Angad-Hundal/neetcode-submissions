class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        res = 0
        seen = set()


        for right in range(len(s)):
            while s[right] in seen:
                # example abcb
                # left = a
                # and right comes to last b
                # then it will first remove a
                # and then b 
                # then there will be no b in the set
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            if (right - left) >= res:
                res = right - left + 1
        
        return res