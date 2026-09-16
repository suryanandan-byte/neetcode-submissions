class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        a=defaultdict(bool)
        l,r=0,0
        c=1
        k=0
        while l<=r and r<len(s):
            if not a[s[r]]:
                a[s[r]]=True
                r+=1
            else:
                a[s[l]]=False
                l+=1
            c=max(c,r-l)
        return c