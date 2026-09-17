# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # go through each element of the head
    # and connect the new elements'next to the previous list that we had 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        res = ListNode(head.val)
        head = head.next

        while head.next:
            res = ListNode(head.val, res)
            head = head.next
        
        res = ListNode(head.val, res)
        
        return res
        