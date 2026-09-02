class Solution:
    def isPalindrome(self, s: str) -> bool:

        # merge the string
        # reverse the string
        # if still the same as original
        # return True else False

        if not s:
            return True
        
        no_space = ""

        for c in s:
            if c.isalnum():
                no_space += c.lower()
        

        if no_space[::-1] ==  no_space:
            return True
        return False

        


        