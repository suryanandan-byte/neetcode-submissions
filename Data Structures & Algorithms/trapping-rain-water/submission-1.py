class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefix,suffix=[0]*n,[0]*n
        m=0
        for i in range(n):
            prefix[i]=m
            m=max(m,height[i])
        m=0
        for i in range(len(height)-1,-1,-1):
            suffix[i]=m
            m=max(m,height[i])
        k=0
        for i in range(1,n-1):
            if suffix[i]-height[i]>0 and prefix[i]>height[i]:
                k+=min(prefix[i]-height[i],suffix[i]-height[i])
        return k