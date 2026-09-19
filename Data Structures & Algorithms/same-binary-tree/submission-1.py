# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # bfs
    # make two queues
    # and put both roots in seperate
    # while both queues exist
    # popleft() and compare
    # append left and right nd continue

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        elif p and not q:
            return False
        elif q and not p:
            return False
        
        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:
            pop_p = queue_p.popleft()
            pop_q = queue_q.popleft()

            if pop_p.val != pop_q.val:
                return False
            
            if (pop_p.left is None) != (pop_q.left is None):
                return False

            if (pop_p.right is None) != (pop_q.right is None):
                return False    

            
            if pop_p.left:
                queue_p.append(pop_p.left)
            if pop_p.right:
                queue_p.append(pop_p.right)
            if pop_q.left:
                queue_q.append(pop_q.left)
            if pop_q.right:
                queue_q.append(pop_q.right)
        
        if queue_p or queue_q:
            return False
            

        return True
        

    