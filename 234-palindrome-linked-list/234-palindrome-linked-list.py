# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = []
        node = head
        while node is not None:
            list.append(node.val)
            node = node.next
        n = len(list)
        for i in range(n//2):
            if list[i] != list[n-1-i]:
                return False
        return True