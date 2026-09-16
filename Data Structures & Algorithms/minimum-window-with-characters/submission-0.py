class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" :
            return ""
        a,b={},{}
        for i in t:
            b[i]=1+b.get(i,0)
        have,need=0,len(b)
        res,leng=[-1,-1],float("infinity")
        l=0
        for i in range(len(s)):
            a[s[i]]=1+a.get(s[i],0)
            if s[i] in b and a[s[i]]==b[s[i]]:
                have+=1
            while have==need:
                if (i-l+1)<leng:
                    res=[l,i]
                    leng=i-l+1
                a[s[l]]-=1
                if s[l]in b and a[s[l]]<b[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if leng!=float("infinity") else ""