class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        mapping = {}

        for num in range(numCourses):
            mapping[num] = []
        
        for num, pre in prerequisites:
            mapping[num].append(pre)
        
        res = []
        visit = set()


        def dfs(num):
            if num in visit:
                return False
            if mapping[num] == []:
                if not num in res:
                    res.append(num)
                return True
            
            visit.add(num)
            
            for pre in mapping[num]:
                if not dfs(pre):
                    return False
                
            visit.remove(num)
            mapping[num] = []
            res.append(num)

            return True
    
            


        for num in range(numCourses):
            if not dfs(num):
                return []
        
        return res


        