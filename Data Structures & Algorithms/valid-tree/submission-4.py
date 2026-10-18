class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n-1:
            return False # cycle
        
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

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for neigh in adj.get(node, []):
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False
                
            return True
        
        return dfs(0,-1) and len(visit) == n
        
        