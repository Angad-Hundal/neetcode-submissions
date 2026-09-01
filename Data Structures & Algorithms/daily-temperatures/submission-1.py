class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] # (index, temp)

        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                pop_i, pop_temp = stack.pop()
                res[pop_i] = ind - pop_i
            stack.append((ind, temp))
        
        return res
        