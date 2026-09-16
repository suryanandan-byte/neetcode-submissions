# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        d=[]
        for i in lists:
            while i:
                d.append(i)
                i=i.next
        if not d:
            return None
        d.sort(key=lambda x:x.val)
        for i in range(len(d)-1):
            d[i].next=d[i+1]
        d[len(d)-1]=None
        return d[0]
