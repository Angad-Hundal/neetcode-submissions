class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        
        num = edges[-1][-1]
        mapping = {}

        for n in range(1, num+1):
            mapping[n] = []
        
        for start, end in edges:
            mapping[start].append(end)
            mapping[end].append(start)
        
        repeat = []
        visit = set()


        def dfs(n):
            # if n in visit:
            #     return
            
            visit.add(n)

            for neigh in mapping[n]:
                if neigh in visit:
                    repeat.append([n, neigh])
                    continue
                dfs(neigh)


        dfs(1)
        print(repeat)
        return repeat[-1]


        