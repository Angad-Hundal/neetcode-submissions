class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] # (index, temp)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                pop_i, pop_t = stack.pop()
                res[pop_i] = idx - pop_i
            stack.append((idx, temp))
    
        return res

        