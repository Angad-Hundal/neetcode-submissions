class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        mapping = {}

        for num in range(n):
            mapping[num] = []
        
        for start, end in edges:
            mapping[start].append(end)
            mapping[end].append(start)
        
        visit = set()
        count = 0

        def dfs(num):

            if num in visit:
                return
            
            visit.add(num)
            
            for neigh in mapping[num]:
                dfs(neigh)

            return 

        for num in range(n):
            if num not in visit:
                dfs(num)
                count += 1



        return count
        

        


            



        