# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(l):
            if not l:
                return "0"
            
            res_str = ""

            curr = l

            while curr:
                res_str += str(curr.val)
                curr = curr.next
            
            return int(res_str[::-1])
        
        first = reverse(l1)
        second = reverse(l2)

        plus = first + second


        def make_list(plus: int):
            plus = str(plus)[::-1]

            res = Node(0)

            for char in plus:
                res.next = char
                res = res.next
            
            return res.next
        
        return make_list(plus)






        