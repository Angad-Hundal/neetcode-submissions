"""
1. Build the adjacency list:
   Create a graph containing all the edges. Since this is an undirected graph,
   add each edge in both directions.

2. Start from the last edge:
   Iterate through the edges in reverse order because we want to find the
   last redundant edge.

3. Temporarily remove the current edge:
   Remove the connection from both nodes in the adjacency list.

4. Run DFS:
   Start DFS from the first node (start) and try to reach the second node (end).

   - Pass end as the target to DFS.
   - If the current node equals target, return True.
   - If the current node has already been visited, return False.
   - Otherwise, mark it as visited and explore its neighbours.

5. Check the result:
   - If DFS returns True, another path exists between the two endpoints.
     Therefore, the removed edge is redundant. Return it.
   - If DFS returns False, no alternative path exists.
     Restore the edge and continue checking the previous edge.

6. Repeat:
   Continue until we find the redundant edge.
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        num = max(max(edge) for edge in edges)

        mapping = {n: [] for n in range(1, num + 1)}

        for start, end in edges:
            mapping[start].append(end)
            mapping[end].append(start)

        visit = set()

        def dfs(n, target):
            if n == target:
                # we reached the tager
                # confirming that there the start, end is not needed
                return True

            if n in visit:
                return False

            visit.add(n)

            for neigh in mapping[n]:
                if dfs(neigh, target):
                    return True

            return False

        for start, end in reversed(edges):

            mapping[start].remove(end)
            mapping[end].remove(start)

            visit.clear()
            target = end

            if dfs(start, target):
                # the cycle exist even after removing this edge
                # so this edgne not needed
                return [start, end]

            mapping[start].append(end)
            mapping[end].append(start)