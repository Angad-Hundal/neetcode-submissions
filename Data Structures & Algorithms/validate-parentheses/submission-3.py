class Solution:
    def isValid(self, s: str) -> bool:

        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # make a stack
        # check the char in s
        # if char not in close_to_open: then it is opening char
        # append the char in stack

        # if char is in close_to_open: it is a closing char
        # and id stack empty -> return false
        # else pop the element and if that element == close_to_open_value then good
        # else return False
        # in end if stack contain anything return False
        # return True


        stack = []

        for char in s:
            if not char in close_to_open:
                stack.append(char)
            else:
                # char is closing one
                if not stack:
                    return False
                element = stack.pop()
                if element != close_to_open[char]:
                    return False
                
        if stack:
            return False
        return True
                


        