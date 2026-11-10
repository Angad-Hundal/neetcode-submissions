class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        mapping = {}

        for num in range(numCourses):
            mapping[num] = []

        for c,p in prerequisites:
            mapping[c].append(p)
        

        visit = set()


        def dfs(num):
            if num in visit:
                return False
            if mapping[num] == []:
                return True
            
            visit.add(num)

            for pre in mapping[num]:
                if not dfs(pre):
                    return False
            
            visit.remove(num)
            mapping[num] = []
            return True

        

        for num in range(numCourses):
            if not dfs(num):
                return False
        

        return True

        

