class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def apply(first: int, second: int, symbol: str) -> int:
            if symbol == "+":
                return first + second
            elif symbol == "-":
                return first - second
            elif symbol == "*":
                return first*second
            elif symbol == "/":
                return int(first/second)
        


        stack = []


        for ele in tokens:
            if ele in {"+", "-", "*", "/"}:
                second = int(stack.pop())
                first = int(stack.pop())

                result = apply(first, second, ele)

                stack.append(result)
            else:
                stack.append(ele)
        
        return int(stack.pop())




