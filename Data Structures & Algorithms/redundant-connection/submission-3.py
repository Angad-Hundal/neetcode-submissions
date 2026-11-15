class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num = max(max(edge) for edge in edges)

        mapping = {n: [] for n in range(1, num + 1)}

        for start, end in edges:
            mapping[start].append(end)
            mapping[end].append(start)

        visit = set()
        repeat = []

        def dfs(parent, n):
            visit.add(n)

            for neigh in mapping[n]:
                if neigh == parent:
                    continue

                if neigh in visit:
                    repeat.append([n, neigh])
                    continue

                dfs(n, neigh)

        dfs(-1, 1)

        return repeat[-1]