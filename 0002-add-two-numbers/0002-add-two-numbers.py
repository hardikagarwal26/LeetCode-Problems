# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            sum=carry
            if l1 is not None:
                sum = sum+l1.val
                l1 = l1.next
            if l2 is not None:
                sum = sum+ l2.val
                l2 = l2.next
            carry = sum // 10
            curr.next = ListNode(sum%10)
            curr = curr.next
        return dummy.next

        