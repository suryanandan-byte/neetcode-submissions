# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        n=1
        tail=head
        while tail.next:
            tail=tail.next
            n+=1
        k%=n
        a=n-k
        tail.next=head
        curr=head
        for _ in range(a-1):
            curr=curr.next
        head=curr.next
        curr.next=None
        return head
        