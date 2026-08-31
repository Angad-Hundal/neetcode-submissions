class Solution:

    def apply(self, first: int, second: int, symbol: str) -> int:

        if symbol == "+":
            return first + second
        elif symbol == "-":
            return first - second
        elif symbol == "*":
            return first*second
        elif symbol == "/":
            return first//second
    
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                second = int(stack.pop())
                first = int(stack.pop())
                final = self.apply(first, second, token)
                stack.append(final)

            
            else:
                stack.append(token)
        
        return stack.pop()
