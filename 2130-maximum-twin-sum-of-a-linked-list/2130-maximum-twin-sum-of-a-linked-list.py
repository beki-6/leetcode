# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sums = []
        list = []
        max = -float('inf')
        node = head
        i, j = 0, 0
        while node != None:
            j += 1
            list.append(node.val)
            node = node.next
        n = j
        j = j-1
        while i < j:
            if j == (n-1-i):
                sum = list[i] + list[j]
                if sum > max:
                    max = sum
            i += 1
            j -= 1
        return max