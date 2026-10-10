# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def bfs(root):

            if not root:
                return 0
            
            q = deque([root])

            while q:
                e = q.popleft()
                
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)

                return 1 + max(bfs(e.left), bfs(e.right))



            
        
        return bfs(root)
        