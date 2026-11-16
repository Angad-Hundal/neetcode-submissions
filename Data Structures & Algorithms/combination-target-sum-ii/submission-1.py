class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()
        res = []
        sol = []

        def dfs(idx, total):

            if total == target:
                res.append(sol.copy())
                return

            if idx >= len(candidates) or total > target:
                return

            # Don't pick current candidate
            next_idx = idx + 1

            while (next_idx < len(candidates)
                   and candidates[next_idx] == candidates[idx]):
                next_idx += 1

            dfs(next_idx, total)

            # Pick current candidate
            sol.append(candidates[idx])
            dfs(idx + 1, total + candidates[idx])
            sol.pop()

        dfs(0, 0)
        return res