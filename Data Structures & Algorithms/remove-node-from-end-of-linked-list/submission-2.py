# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # find the total length
        # then the index of the node to remove = length - n
        # then the prev elemtn .next = next.next


        count = 0
        curr = head

        while curr:
            curr = curr.next
            count += 1
        

        index = count - n
        # 1,2,3,4,5,6,7
        # 3rd element = 3
        # count = 6 - 3 = 3

        count = 1

        if index == 0:
            return head.next
        
        curr = head

        while curr:
            if count == index:
                curr.next = curr.next.next
                return head
            count += 1
            curr = curr.next
        