class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        sol = []


        def dfs(idx):
            if idx >= len(nums):
                res.append(sol.copy())
            
            # without idx 
            dfs(idx+1)

            # with idx
            sol.appen(nums[idx])
            dfs(idx+1)
            sol.pop()
        
        dfs(0)
        return res
        