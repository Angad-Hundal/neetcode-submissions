class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []


        def dfs(idx, total):
            if total == target and not sol.copy() in res:
                res.append(sol.copy())
                return
            if idx >= len(candidates) or total > target:
                return
            
            dfs(idx+1, total)

            sol.append(candidates[idx])
            dfs(idx+1, total + candidates[idx])
            sol.pop()

        dfs(0,0)
        return res