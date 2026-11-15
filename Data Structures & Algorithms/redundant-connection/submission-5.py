class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        mapping = {}

        def dfs(start, target, visit):
            if start == target:
                return True

            visit.add(start)

            for neigh in mapping.get(start, []):
                if neigh not in visit:
                    if dfs(neigh, target, visit):
                        return True

            return False

        for start, end in edges:

            # Check if a path already exists between start and end
            if dfs(start, end, set()):
                return [start, end]

            # Add the edge only if it doesn't create a cycle
            mapping.setdefault(start, []).append(end)
            mapping.setdefault(end, []).append(start)