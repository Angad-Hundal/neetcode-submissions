# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque([root])

        res = []

        while q:
            nest = None

            for i in range(len(q)):
                e = q.popleft()
                nest = e.val

                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            
            res.append(nest)
        
        return res


        