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


        def dfs(parent, n):
            if n in visit:
                repeat.append([parent, n])
                return
            
            visit.add((parent, n))

            for neigh in mapping[n]:
                if neigh == n:
                    continue
                dfs(n, neigh)


        dfs(0,1)
        print(repeat)
        return repeat[-1]


        