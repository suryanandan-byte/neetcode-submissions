class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l={}
        for i in nums:
            l[i]=l.get(i,0)+1
            if(l[i]>1):
                return True
        return False
        