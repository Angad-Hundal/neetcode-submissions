# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursion
    # base case: 
    # if not root -> return True
    # if root and not 

    def maxHeight(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)

        return max(left, right) + 1
        


    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        elif root and not root.left and not root.right:
            return True
        
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)

        current = abs(left - right) <= 1

        return current and self.isBalanced(root.left) and self.isBalanced(root.right)


        