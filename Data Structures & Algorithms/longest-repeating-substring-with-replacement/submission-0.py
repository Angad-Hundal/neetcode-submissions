class Solution:

    # keep a hash map for each char count
    # res = max freq
    # left = 0

    # for each r
    # find the count of char on r
    
    # if the window - count > k
    # slide the left element
    # decrease the count of left element

    # res = max(res, the new one)

    # return final result
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        l = 0
        res = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            # num of replacements greater k
            # slide the left
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
            



