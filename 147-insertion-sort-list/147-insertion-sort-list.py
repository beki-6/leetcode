# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        node = head
        while node is not None:
            list.append(node.val)
            node = node.next
        n = len(list)
        for i in range(n):
            key = list[i]
            j = i-1
            while j >= 0 and list[j] > key:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = key
        sortedList = []
        for i in list:
            sortedList.append(ListNode(i))
        newHead = sortedList[0]
        for i in range(n-1):
            sortedList[i].next = sortedList[i+1]
        return newHead