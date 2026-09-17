class Solution:
    def dailyTemperatures(self, num: List[int]) -> List[int]:
        a=[]
        a.append(0)
        b=[0]*(len(num))
        for i in range(1,len(num)):
            if num[a[-1]]>num[i]:
                a.append(i)
            else:
                while a and num[a[-1]]<num[i]:
                    b[a[-1]]=i-a[-1]
                    a.pop()
                a.append(i)
        return b