class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        num = max(max(edge) for edge in edges)

        mapping = {n: [] for n in range(1, num + 1)}

        for start, end in edges:
            mapping[start].append(end)
            mapping[end].append(start)

        visit = set()
        target = None

        def dfs(n):
            if n == target:
                return True

            visit.add(n)

            for neigh in mapping[n]:
                if neigh not in visit:
                    if dfs(neigh):
                        return True

            return False

        for start, end in reversed(edges):

            mapping[start].remove(end)
            mapping[end].remove(start)

            visit.clear()
            target = end

            if dfs(start):
                return [start, end]

            mapping[start].append(end)
            mapping[end].append(start)