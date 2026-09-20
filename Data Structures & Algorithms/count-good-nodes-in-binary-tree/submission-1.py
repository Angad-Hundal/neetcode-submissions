# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # use DFS
    # for root -> 1
    # [res, max] till now
    # 
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        res = 0

        queue = deque([(root, -float('inf'))])

        while queue:
            node, max_v = queue.popleft()

            if node.val >= max_v:
                res += 1
            
            if node.right:
                queue.append([node.right, max(max_v, node.val)])
            if node.left:
                queue.append([node.left, max(max_v, node.val)])
        
        return res
        