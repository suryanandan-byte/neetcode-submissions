class Solution:
    def removeElement(self, a: List[int], val: int) -> int:
        l,n = 0,len(a)-1
        while(l<=n):
            if a[l]==val:
                if a[n]!=val:
                    a[l]=a[n]
                    n-=1
                    l+=1
                else:
                    n-=1
            else:
                l+=1
        return l