# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        noneNode = ListNode()
        sum = []
        while l1 or l2 or carry != 0:
            cur = ListNode()
            print(carry)
            if l1 is None and l2 is None and carry == 0:
                return
            elif l1 is None and l2 is None:
                l1 = noneNode
                l2 = noneNode
            elif l1 is None:
                l1 = noneNode
            elif l2 is None:
                l2 = noneNode
            x = carry + l1.val + l2.val
            if x > 9:
                carry = int(x/10)
                x = x%10 
            else:
                carry = 0
            cur.val = x
            sum.append(cur)
            l1 = l1.next
            l2 = l2.next
        head = sum[0]
        for i in range(len(sum)-1):
            if sum[i] is not None:
                sum[i].next = sum[i+1]
        return head