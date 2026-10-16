class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre_map = {}

        for i in range(numCourses):
            pre_map[i] = []

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        visit = set()

        def dfs(crs):

            if crs in visit:
                return False
            if pre_map[crs] == []:
                return True
            
            visit.add(crs)

            for e in pre_map[crs]:
                if not dfs(e):
                    return False

            # visit.remove(crs)
            # pre_map[crs] = []
            return True       

        for e in range(numCourses):
            if not dfs(e):
                return False
            
        return True
            

        