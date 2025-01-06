# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 1
        tail = head
        if head is None or k==0:
            return head
        while tail.next is not None:
            tail = tail.next
            length += 1
        k = k % length
        if k==0:
            return head
        tail.next = head
        temp = head
        for _ in range(length-k-1):
            temp = temp.next
        nhead = temp.next
        temp.next = None
        return nhead
        
        