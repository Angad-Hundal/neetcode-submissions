class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        sol = []


        def dfs(idx, total):
            if total == target:
                res.append(sol.copy())
                return
            if idx>= len(candidates) or total > target:
                return
            

            # pick the num
            sol.append(candidates[idx])
            dfs(idx+1, total+candidates[idx])
            sol.pop()

            # dont pick the number
            
            next_idx = idx+1

            while next_idx < len(candidates) and candidates[idx] == candidates[next_idx]:
                next_idx += 1
            
            dfs(next_idx, total)


        dfs(0,0)
        return res
        