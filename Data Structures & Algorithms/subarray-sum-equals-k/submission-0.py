class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n,m=0,0
        l={0:1}
        for i in nums:
            n+=i
            a=n-k
            m+=l.get(a,0)
            l[n]=1+l.get(n,0)
        return m