class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        c=0
        while l<r :
            c=max(c,(r-l)*min(h[l],h[r]))
            if h[l]>h[r]:
                r-=1
            else:
                l+=1
        return c