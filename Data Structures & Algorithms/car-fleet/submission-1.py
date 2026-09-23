class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l=[]
        for i in range(len(position)):
            l.append((position[i],speed[i]))
        l.sort(reverse=True)
        c=[]
        for i,j in l:
            c.append((target-i)/j)
            if len(c)>=2 and c[-1]<=c[-2]:
                c.pop()
        return len(c)