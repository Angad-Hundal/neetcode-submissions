class Solution:
    # make a string with all 
    # lowercase 
    # the alpha and nums
    # no space
    # and then reverse that string
    # check ==
    def isPalindrome(self, s: str) -> bool:

        front = ""

        for char in s:
            if char.isalnum():
                lower_char = char.lower()
                front += lower_char
        
        return front[::-1] == front

        