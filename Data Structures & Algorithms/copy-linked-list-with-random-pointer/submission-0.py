"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=None
        temp1=head
        head1=None
        mp={}
        while temp1 :
            newnode=Node(temp1.val)
            mp[temp1]=newnode
            if head1 is None:
                head1=temp=newnode
            else:
                temp.next=newnode
                temp=newnode
            temp1=temp1.next
        temp1=head
        while temp1:
            c=mp[temp1]
            c.next=mp[temp1.next] if temp1.next else None
            c.random=mp[temp1.random] if temp1.random else None
            temp1=temp1.next
        return head1