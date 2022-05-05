# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        length = 0
        while node != None:
            length += 1
            node = node.next
        length = int(length/2)
        i = 0
        node = head
        while i < length:
            node = node.next
            i += 1
        return node