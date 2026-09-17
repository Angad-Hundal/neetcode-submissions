class Solution:

    def minWindow(self, s: str, t: str) -> str:

        shortest = s
        sorted_t = "".join(sorted(t))

        for left in range(len(s)):
            for right in range(left, len(s)):
                sorted_chunk = "".join(sorted(s[left:right+1]))

                if sorted_t in sorted_chunk and len(sorted_chunk) < len(shortest):
                    shortest = s[left:right+1]

        if shortest == s:
            return ""

        return shortest