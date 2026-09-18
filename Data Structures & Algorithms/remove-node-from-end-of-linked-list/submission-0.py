class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        index = len(nodes) - n

        # Removing the head
        if index == 0:
            return head.next

        # Removing the last node
        elif index + 1 == len(nodes):
            nodes[index - 1].next = None

        # Removing a node in the middle
        else:
            nodes[index - 1].next = nodes[index + 1]

        return head