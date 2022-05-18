# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2, merged = [], [], []
        node = list1
        while node != None:
            l1.append(node.val)
            node = node.next
        node = list2
        while node != None:
            l2.append(node.val)
            node = node.next
        n1 = len(l1)
        n2 = len(l2)
        i, j = 0, 0
        if n1 < n2:
            n = n1
        else:
            n = n2
        while i < n1 and j < n2:
            if l1[i] <= l2[j]:
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1
        while i < len(l1):
                merged.append(l1[i])
                i += 1
        while j < len(l2):
                merged.append(l2[j])
                j += 1
        nodes = []
        for i in range(len(merged)):
            nodes.append(ListNode(merged[i]))
        for i in range(len(merged)-1):
            nodes[i].next = nodes[i+1]
        if len(nodes) == 0:
            return
        return nodes[0]