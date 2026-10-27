class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        k = len(s1)

        for i in range(len(s2) - k + 1):
            subStr = sorted(s2[i:i + k])

            if subStr == s1:
                return True

        return False