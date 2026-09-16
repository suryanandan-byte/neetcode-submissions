class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        l=[""]
        n,m=0,0
        for i in range(len(s[0])):
            c=0
            for j in range(len(s)):
                if i < len(s[j]) and s[0][i] == s[j][i]:
                    c+=1
                else:
                    break;
            if c==len(s):
                l[0]=l[0]+s[0][i]
            else:
                break
        return l[0]