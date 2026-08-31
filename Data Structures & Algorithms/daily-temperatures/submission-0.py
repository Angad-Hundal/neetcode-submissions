class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        final = []
        
        for index in range(len(temperatures)):
            found = False
            inner_index = index+1
            while inner_index < len(temperatures):
                if temperatures[inner_index] > temperatures[index]:
                    final.append(inner_index-index)
                    found = True
                    break
                inner_index += 1

            if not found:
                final.append(0)
        
        return final




