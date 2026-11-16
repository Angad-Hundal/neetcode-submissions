"""

We are going to use backtracking
We will make a res array
We will make a dfs function where we 
Consider both the approaches: taking the nums[idx] and without taking that number
"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def dfs(idx, total):
            if total == target:
                res.append(sol.copy())
                return

            if idx >= len(nums) or total > target:
                return
            
            dfs(idx+1, total)

            sol.append(nums[idx])
            dfs(idx, total+nums[idx])
            sol.pop()


        dfs(0,0)
        return res