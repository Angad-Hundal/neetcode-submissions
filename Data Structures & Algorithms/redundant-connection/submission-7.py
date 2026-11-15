"""
Build the adjacency list: Create a graph containing all the edges. Since this is an undirected graph, add each edge in both directions.
Start from the last edge: Iterate through the edges in reverse order because we want to find the last edge that can be removed without disconnecting its two endpoints.
Temporarily remove the current edge: Remove the connection from both nodes in the adjacency list.
Run DFS: Start DFS from the first node (start) and try to reach the second node (end).
Check the result:
    - If DFS reaches end, it means another path already exists between the two nodes. Therefore, the removed edge is redundant. Return it.
    - If DFS cannot reach end, it means that edge is necessary to keep the two nodes connected. Restore the edge and continue checking the previous edge.

Repeat: Continue until we find the redundant edge.
"""

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