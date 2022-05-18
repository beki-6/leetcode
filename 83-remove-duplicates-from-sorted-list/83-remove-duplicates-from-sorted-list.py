# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if node == None:
            return 
        while node.next != None:
            while node.next != None and node.val == node.next.val:
                node.next = node.next.next
            if node.next != None:
                node = node.next
            else:
                break
        return head