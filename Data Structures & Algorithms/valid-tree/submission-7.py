class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        mapping = {i: [] for i in range(n)}

        for a, b in edges:
            mapping[a].append(b)
            mapping[b].append(a)

        visit = set()

        def dfs(num):
            if num in visit:
                return
            
            visit.add(num)

            for end in mapping[num]:
                # ideally we should check if the num == end 
                # we going over same path and shall continue
                # but if num in visit already check that
                dfs(end)

        dfs(0)

        return len(visit) == n