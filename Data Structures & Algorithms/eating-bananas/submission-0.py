class Solution:
    def binary(self,nums:List[int],h:int,l:int,r:int):
        c=r
        while l<=r:
            mid=(l+r)//2
            x=0
            for i in nums:
                x+=math.ceil((float(i))/mid)
            if x<=h:
                c=mid
                r=mid-1
            else:
                l=mid+1
        return c
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.binary(piles,h,1,max(piles))