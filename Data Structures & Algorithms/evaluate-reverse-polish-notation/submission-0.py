class Solution:
    # let us try with stack 
    # make a stack: reverse the list
    # pop two numbers
    # and then pop the symbol
    # do the operation (make function for it)
    # pop the second element 
    # while loop 
    # O(n) time complexity 


    def apply(self, first: int, second: int, symbol: str) -> int:

        if symbol == "+":
            return first + second
        elif symbol == "-":
            return first - second
        elif symbol == "*":
            return first*second
        elif symbol == "/":
            return first/second

    def evalRPN(self, tokens: List[str]) -> int:

        tokens.reverse()

        first = int(tokens.pop())

        while tokens:
            second = int(tokens.pop())
            symbol = tokens.pop()
            first = self.apply(first, second, symbol)

        return first 






        