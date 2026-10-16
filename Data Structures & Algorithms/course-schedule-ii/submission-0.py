class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        pre_map = {}

        for i in range(numCourses):
            pre_map[i] = []

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        visit, cycle = set(), set()
        output = []

        def dfs(crs):

            if crs in visit:
                return True
            if crs in cycle:
                return False
            
            # visit.add(crs)
            cycle.add(crs)

            for e in pre_map[crs]:
                if not dfs(e):
                    return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True       

        for e in range(numCourses):
            if not dfs(e):
                return []
            
        return output
        