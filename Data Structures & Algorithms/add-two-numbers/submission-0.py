class Solution:

    def convert(self, l: Optional[ListNode]):
        res = ""

        curr = l
        
        while curr:
            res += str(curr.val)
            curr = curr.next
        
        res = res[::-1]

        return int(res)
    
    def convertBack(self, num: int) -> Optional[ListNode]:

        num_s = str(num)

        res = None

        for char in num_s:
            res = ListNode(int(char), res)
        
        return res


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = self.convert(l1)
        num2 = self.convert(l2)

        final = num1 + num2

        return self.convertBack(final)