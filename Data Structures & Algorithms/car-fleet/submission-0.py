class Solution:
    # p = [4,1,0,7]
    # s = [2,2,1,1]
    # 1 = [6,3,1,8]
    # 2 = [8,5,2,9]
    # 3 =[10,7,3,10]
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        zipped = []

        for p, s in zip(position, speed):
            zipped.append((p,s))
        
        zipped.sort(reverse=True)

        time_stack = []

        for p,s in zipped:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)


        
        