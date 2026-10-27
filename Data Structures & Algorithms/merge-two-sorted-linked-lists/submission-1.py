# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None
        
        res = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                res = ListNode(res, list1.val)
            else:
                res = ListNode(res, list2.val)
        
        while list1:
            res = ListNode(res, list1.val)
        
        while list2:
            res = ListNode(res, list2.val)
        
        return res


