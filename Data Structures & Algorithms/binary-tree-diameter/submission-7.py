# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(root):

            nonlocal res 

            if not root:
                return 0
            
            # max height left and right
            left = dfs(root.left)
            right = dfs(root.right)

            # max of res or left + right height
            res = max(left+right, res)

            # return max height at the node
            return 1+ max(left, right)

        # will just give the height so cant return it
        dfs(root)
        return res
        