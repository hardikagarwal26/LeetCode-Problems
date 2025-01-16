# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        maxval = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        while prev:
            maxval = max(maxval , head.val+prev.val)
            prev = prev.next
            head = head.next
        return maxval

        