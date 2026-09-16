# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        temp=head
        prev=None
        while temp.next is not None:
            k=temp.next
            temp.next=prev
            prev=temp
            temp=k
        temp.next=prev
        head=temp
        return head