class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]):

        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            # stack not there
            # the time for car at lower position
            # is greater than car furher ahead
            # car at lower position gonna take more time 
            if not stack or time > stack[-1]:
                stack.append(time)
            # else
            # car is gonna take less time 
            # therefore merging with the fleet in front

        return len(stack)