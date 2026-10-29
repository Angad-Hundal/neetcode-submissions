# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None
        
        temp = head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        index = count - n

        if index == 0:
            head = head.next
            return head

        temp = head
        pos = 1

        while temp:
            if pos != index:
                temp = temp.next
                pos += 1
            else:
                # Remove the next node
                temp.next = temp.next.next
                return head

        return head