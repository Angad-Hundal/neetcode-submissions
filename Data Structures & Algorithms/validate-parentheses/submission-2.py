class Solution:
    # form a stack
    # keep on appending the opening ones
    # if u see the closing one, check if the stack top is the same closing one
    # if yes, pop that
    # if not, then return False
    # if the stack is all popped in the end then True
    # else False
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in {"[", "{", "("}:
                stack.append(char)
            elif stack:
                pop = stack.pop()
                
                if char == ")" and pop != "(":
                    return False
                elif char=="]" and pop != "[":
                    return False
                elif char=="}" and pop != "{":
                    return False
            else:
                return False
                
        if len(stack) > 0:
            return False
        
        return True


        