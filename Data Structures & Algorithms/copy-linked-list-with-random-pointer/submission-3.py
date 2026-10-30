"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        store = {}

        curr = head

        # create copy
        while curr:
            store[curr] = Node(curr.val)
            curr = curr.next
        

        curr = head

        while curr:
            # stored value.next = curr.next but in store
            store[curr].next = store.get(curr.next)
            store[curr].random = store.get(curr.random)
            curr = curr.next
        
        return store[head]

        

