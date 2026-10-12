# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            if not root:
                return True
            
            right = dfs(root.right)
            left = dfs(root.left)

            if abs(right - left) >= 1:
                return False
            
            return True
        
        return dfs(root)

        