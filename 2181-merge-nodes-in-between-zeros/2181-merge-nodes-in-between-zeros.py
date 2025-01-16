# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        prev = head.next
        s = 0
        while curr:
            x = curr.val
            if x!=0:
                s+=x
            else:
                prev.val = s
                prev.next = curr.next
                prev = prev.next
                s=0
            curr = curr.next
        return head.next
        