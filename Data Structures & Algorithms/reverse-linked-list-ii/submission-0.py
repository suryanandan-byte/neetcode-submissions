# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp=head
        prev=None
        c=0
        while temp:
            if c==left-1:
                break
            c+=1
            prev=temp
            temp=temp.next
        head1=temp
        for i in range(left-1,right-1):
            temp=temp.next
        head2=temp.next
        temp.next=None
        temp=head1
        prev1=head2
        while temp:
            curr=temp.next
            temp.next=prev1
            prev1=temp
            temp=curr
        if prev:
            prev.next=prev1
        if left==1:
            return prev1
        return head