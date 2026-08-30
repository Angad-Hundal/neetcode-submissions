class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_num:
            self.min_num = val
        

    def pop(self) -> None:
        if self.stack:
            num = self.stack[-1]
            if num == self.min_num:
                self.min_num = min(self.stack)
            self.stack.pop(-1)
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_num
        
