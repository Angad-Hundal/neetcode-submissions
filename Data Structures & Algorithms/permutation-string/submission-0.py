class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1 = sorted(s1)

        for left in range(len(s2)):
            for right in range(left, len(s2)):
                chunk = s2[left: right + 1]
                chunk = sorted(chunk)
                if chunk == s1:
                    return True
        
        return False


        