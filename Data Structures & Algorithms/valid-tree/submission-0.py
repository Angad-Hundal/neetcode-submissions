class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # more dges than the nodes; so cycle there
        if len(edges) > (n-1):
            return False
        
        adj = []
        for _ in range(n):
            adj.append([])

        # at index i; we have all nodes it is connected to
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for neig in adj[node]:
                if neig == prev:
                    continue
                if not dfs(neig, node):
                    return False
            return True
        

        return dfs(0, -1) and len(visit) == n