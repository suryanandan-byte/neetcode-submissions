class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        l=set()
        for i in nums:
            if count[i]>len(nums)//3:
                l.add(i)
        return list(l)