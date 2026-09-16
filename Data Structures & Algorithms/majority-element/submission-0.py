class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=collections.defaultdict(list)
        for i in nums:
            l[i]=l.get(i,0)+1
        m=0
        k=0
        for i,j in l.items():
            if(j>m):
                m=j
                k=i
        return k