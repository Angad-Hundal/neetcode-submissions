class Solution:

    # make a hash from close to open
    # make an empty stack
    
    # for all char in s
    # if char not in hash (opening)
    # push on stack
    
    # if char on stack (closing)
    # keep on popping 

    def isValid(self, s: str) -> bool:

        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for char in s:
            
            # opening 
            if not char in closeToOpen:
                stack.append(char)
            else: 
                # closing
                if not stack:
                    return False
                element = stack.pop()
                if element != closeToOpen[char]:
                    return False
        
        if stack:
            return False
        
        return True
            

        