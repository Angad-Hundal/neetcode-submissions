class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True

        close_open = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        for char in s:

            if not char in close_open:
                stack.append(char)
            else:
                if not stack:
                    return False
                element = stack.pop()
                if element != close_open[char]:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True

        

        