# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # BFS
    # make a list and a queue
    # while queue
    # pop from the queue
    # append the value in the list
    # append the left and right in the queue
    # return the list

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        

        queue = deque([root])
        res = []

        while queue:
            nest = []

            for i in range(len(queue)):
                pop = queue.popleft()
                nest.append(pop.val)

                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
            
            res.append(nest)
        
        return res


        