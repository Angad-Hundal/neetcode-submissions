class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        curr = head
        res = {}

        # First pass: Create a copy of every node
        while curr:
            res[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: Connect next and random pointers
        curr = head

        while curr:
            res[curr].next = res.get(curr.next)
            res[curr].random = res.get(curr.random)
            curr = curr.next

        return res[head]