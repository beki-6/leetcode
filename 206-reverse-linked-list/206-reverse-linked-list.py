# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        nodes = []
        node = head
        while node != None:
            list.append(node.val)
            node = node.next 
        list = list[::-1]
        for i in list:
            nodes.append(ListNode(i))
        n = len(nodes)-1
        for i in range(n):
            nodes[i].next = nodes[i+1]
        if len(nodes) == 0:
            return
        return nodes[0]