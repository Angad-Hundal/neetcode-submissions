class Solution:
    def mergeTwoLists(self, list1, list2):
        res = ListNode(None)
        curr = res

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next

            curr = curr.next

        while list1:
            curr.next = ListNode(list1.val)
            list1 = list1.next
            curr = curr.next

        while list2:
            curr.next = ListNode(list2.val)
            list2 = list2.next
            curr = curr.next

        return res.next