class Solution:
    def simplifyPath(self, path: str) -> str:
        l=[]
        paths=path.split("/")
        for i in paths:
            if i =='..':
                if l:
                    l.pop()
            elif i!="" and i!=".":
                l.append(i)
        return '/'+'/'.join(l)