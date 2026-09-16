class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=defaultdict(int)
        res=0
        for i in nums:
            if not l[i]:
                l[i]=l[i-1]+l[i+1]+1
                l[i-l[i-1]]=l[i]
                l[i+l[i+1]]=l[i]
                res=max(res,l[i])
        return res