# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next
        l=l-n
        temp=head
        prev=None
        if l==0:
            return head.next
        else:
            for i in range(l-1):
                temp=temp.next
            temp.next=temp.next.next
            return head