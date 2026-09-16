class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c=[]
        for i in range(min(len(word1),len(word2))):
            c.append(word1[i])
            c.append(word2[i])
        if len(word1)>len(word2):
            c.extend(list(word1[i+1:]))
        elif len(word1)<len(word2):
            c.extend(list(word2[i+1:]))
        l=""
        for i in c:
            l+=i
        return l