class Solution:
    def numRescueBoats(self, a: List[int], k: int) -> int:
        a.sort()
        c=0
        i,r=0,len(a)-1
        while i<=r:
            diff=k-a[r]
            r-=1
            c+=1
            if i<=r and diff>=a[i]:
                i+=1
            
        return c  