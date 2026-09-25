class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        l,r=max(nums),sum(nums)
        res=r
        def canShip(c):
            ship,currcap=1,c
            for i in nums:
                if currcap-i<0:
                    ship+=1
                    if ship>days:
                        return False
                    currcap=c
                currcap-=i
            return True
        while l<=r:
            mid =(l+r)//2
            if canShip(mid):
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res