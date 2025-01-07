# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self,head:ListNode)->ListNode:
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        nmid = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(nmid)
        return self.merge(left,right)
    def merge(self , left:ListNode , right:ListNode) ->ListNode:
        dm = ListNode(0)
        tail = dm
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        else :
            tail.next = right
        return dm.next

        