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
                # already visited
                return False
            
            visit.add(node)

            for neig in adj[node]:
                # Got to 1 from 0
                # do not have to check 0 back
                if neig == prev:
                    continue
                if not dfs(neig, node):
                    return False
            return True
        
        # check len to make sure no node is disconnected
        # -1 because the ndoes start at 0
        return dfs(0, -1) and len(visit) == n