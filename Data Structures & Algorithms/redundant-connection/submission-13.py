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

        nums = [max(edge) for edge in edges]
        num = max(nums)

        mapping = {}

        for n in range(1, num+1):
            mapping[n] = []
        
        for start, end in edges:
            mapping[start].append(end)
            mapping[end].append(start)


        def dfs(start, target, visit):
            if start in visit:
                return False
            
            if start == target:
                return True
            
            visit.add(start)
            
            for neigh in mapping[start]:
                if dfs(neigh, end, visit):
                    return True
            
            return False


        for start, end in reversed(edges):
            mapping[start].remove(end)
            mapping[end].remove(start)

            visit = set()
            if dfs(start, end, visit):
                return [start, end]
            
            mapping[start].append(end)
            mapping[end].append(start)
            
        
        return []



