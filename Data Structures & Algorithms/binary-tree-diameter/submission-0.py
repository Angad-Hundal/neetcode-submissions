# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxHeight(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)

        return max(left, right) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)      

        diameter = leftHeight + rightHeight

        sub =  max(self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))

        return max(sub, diameter)
        