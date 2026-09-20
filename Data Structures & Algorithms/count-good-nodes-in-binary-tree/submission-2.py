# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0

        def dfs(root:TreeNode, max_value: int):
            nonlocal res

            if not root:
                return 
            
            if root.val >= max_value:
                res += 1
            
            max_value = max(max_value, root.val)
            self.dfs(root.right, max_value)
            self.dfs(root.left, max_value)
            
        return res
            

            

        