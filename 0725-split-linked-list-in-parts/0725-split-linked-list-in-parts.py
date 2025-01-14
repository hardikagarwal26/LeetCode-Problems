# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n=0
        curr = head
        while curr:
            n+=1
            curr=curr.next
        
        base = n//k
        left = n%k

        ans=[]
        curr=head
        for i in range(k):
            nh = curr
            psize = base + (1 if left>0 else 0)
            left-=1

            for _ in range(psize-1):
                if curr:
                    curr = curr.next
            if curr:
                npart = curr.next
                curr.next = None
                curr = npart
            ans.append(nh)
        return ans



        