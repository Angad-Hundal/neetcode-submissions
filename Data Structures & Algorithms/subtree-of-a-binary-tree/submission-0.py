# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    # use DFS

    def isSame(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root and not subroot:
            return True
        elif not root or not subroot:
            return False
        elif root.val != subroot.val:
            return False
        return self.isSame(root.right, subroot.right) and self.isSame(root.left, subroot.left)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
