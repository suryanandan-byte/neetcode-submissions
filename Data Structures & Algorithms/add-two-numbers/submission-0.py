# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=temp=None
        temp1=l1
        temp2=l2
        carry=0
        while temp1!=None or temp2!=None:
            newNode=ListNode(0)
            a=0 if not temp1  else temp1.val
            b=0 if not temp2  else temp2.val
            if head==None:
                head=temp=newNode
            else:
                temp.next=newNode
                temp=newNode
            temp.val=(a+b+carry)%10
            carry=(a+b+carry)//10
            temp1=temp1.next if temp1 else None
            temp2=temp2.next if temp2 else None
        if carry!=0:
            newNode=ListNode(carry)
            temp.next=newNode
        return head