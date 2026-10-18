class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if len(edges) == 0:
            return n
        
        adj = {}

        for u,v in edges:
            if u in adj:
                adj[u].append(v)
            else:
                adj[u] = [v]
            
            if v in adj:
                adj[v].append(u)
            else:
                adj[v] = [u]
        
        visit = set()

        count = 0


        def dfs(node):
            if node in visit:
                return 
            
            visit.add(node)
            for neigh in adj.get(node, []):
                dfs(neigh)



        # loop onto range(len(n))
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)
        
        return count 
        