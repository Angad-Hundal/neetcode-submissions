class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        res = None

        while head:
            res = ListNode(head.val, res)
            head = head.next

        return res