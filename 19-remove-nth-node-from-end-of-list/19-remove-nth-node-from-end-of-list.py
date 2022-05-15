# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        while node != None:
            node = node.next
            length += 1
        x = length - n
        if x == 0:
            return head.next
        i = 0
        prev = head
        cur = head
        while i < x:
            cur = cur.next
            if i == x-2:
                prev = cur
            i += 1
        prev.next = cur.next
        return head