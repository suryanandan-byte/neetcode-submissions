# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head: Optional[ListNode])->None:
        temp=head
        prev=None
        while temp is not None:
            curr=temp.next
            temp.next=prev
            prev=temp
            temp=curr
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        l,r=head,head
        while r and  r.next :
            l=l.next
            r=r.next.next
        r=l
        l=l.next
        r.next=None
        l=self.reverse(l)
        r=head
        while l is not None:
            curr=r.next
            r.next=l
            l=l.next
            r.next.next=curr
            r=curr