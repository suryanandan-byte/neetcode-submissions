class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        for i in s:
            if i=='[':
                stack.append(i)
            elif i==']' and not stack:
                stack.append(i)
            else:
                stack.pop()
        c=len(stack)
        return (c+1)//2