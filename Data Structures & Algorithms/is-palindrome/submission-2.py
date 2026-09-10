class Solution:
    # front_index = 0 and 
    # end_index = len(s)
    # iterate both untill start_index == end_index
    # if the value at start_index.lower() != end_index.lower()
    # return False
    # if the value at the index is not alpha or numberic
    # isalnum -> then change the index

    def isPalindrome(self, s: str) -> bool:
        start_index = 0
        end_index = len(s) -1

        while start_index < end_index:
            if not s[start_index].isalnum():
                start_index += 1
            elif not s[end_index].isalnum():
                end_index -= 1
            elif s[start_index].lower() != s[end_index].lower():
                return False
            else:
                start_index += 1
                end_index -= 1
        
        return True
        