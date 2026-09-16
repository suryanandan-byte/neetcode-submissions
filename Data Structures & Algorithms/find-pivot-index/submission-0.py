class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=[0]*(len(nums)+1)
        for i in range(len(nums)):
            l[i+1]=l[i]+nums[i]
        for i in range(len(nums)):
            n=l[i]
            m=l[len(nums)]-l[i+1]
            if n==m:
                return i
        return -1