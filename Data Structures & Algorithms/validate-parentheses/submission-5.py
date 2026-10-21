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
            if char in close_open:
                element = stack.pop()
                if element == close_open[char]:
                    continue
                else:
                    return False
                
            stack.append(char)
        
        if len(stack) > 0:
            return False
        
        return True

        

        