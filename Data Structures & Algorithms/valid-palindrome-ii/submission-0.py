class Solution:
    def validPalindrome(self, s: str) -> bool:
        k=list(s)
        if s==s[::-1]:
            return True
        for i in range(len(k)):
            m=k[:i]+k[i+1:]
            if m==m[::-1]:
                return True
        return False