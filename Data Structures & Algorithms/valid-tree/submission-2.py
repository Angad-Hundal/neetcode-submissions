class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # more dges than the nodes; so cycle there
        if len(edges) > (n-1):
            return False

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