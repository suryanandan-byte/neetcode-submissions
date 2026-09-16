class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=collections.defaultdict(int)
        for i in nums:
            l[i]+=1
        m=sorted(l.items(),key=lambda x:x[1],reverse=True)
        return [x[0] for x in m[:k]]
        