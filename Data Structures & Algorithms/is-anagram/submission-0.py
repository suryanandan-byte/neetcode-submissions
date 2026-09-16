class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=list(s)
        k=list(t)
        l.sort()
        k.sort()
        return l==k
        