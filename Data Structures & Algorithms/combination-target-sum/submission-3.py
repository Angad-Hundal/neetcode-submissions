class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        sol = []

        def dfs(idx, total):

            # We found a valid combination
            if total == target:
                res.append(sol.copy())
                return

            # Invalid path
            if idx >= len(nums) or total > target:
                return

            # Option 1: Skip the current number
            dfs(idx + 1, total)

            # Option 2: Include the current number
            # important: not idx+1 here
            sol.append(nums[idx])
            dfs(idx, total + nums[idx])
            sol.pop()

        dfs(0, 0)
        return res