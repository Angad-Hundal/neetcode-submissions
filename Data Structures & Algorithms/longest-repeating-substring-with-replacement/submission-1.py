class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0

        for left in range(len(s)):
            count = {}
            maxfreq = 0

            for right in range(left, len(s)):
                count[s[right]] = count.get(s[right], 0) + 1
                maxfreq = max(maxfreq, count[s[right]])

                if (right-left+1) - maxfreq <= k:
                    res = max(res, right-left+1)
        return res
                