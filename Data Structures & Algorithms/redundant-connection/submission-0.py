class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # graph is cyclic
        # remove one 

        n = len(edges)
        adj = [[] for _ in range(n + 1)]


        def dfs(node, prev):
            if visit[node]:
                return True
            

            visit[node] = True

            for neigh in adj[node]:
                if neigh == prev:
                    continue
                if dfs(neigh, node):
                    return True
            
            return False


        # make adj array
        # make a visit array
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (n + 1)

            if dfs(u, -1):
                return [u, v]
        
        return []