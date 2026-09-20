# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # BFS but only append the right most 
    # element at that level in the result
    # make a res list
    # and a queue
    # while queue
    # append the last element in the res index (len(q) - 1)


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        queue = deque([root])
        res = []

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(node.val)
        
        return res
        