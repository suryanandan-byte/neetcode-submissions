class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s1):
            return False
        l=len(s1)
        i=0
        while i+l<=len(s2):
            m=list(s2[i:i+l])
            n=list(s1)
            m.sort()
            n.sort()
            if m==n:
                return True
                break
            i+=1
        return False