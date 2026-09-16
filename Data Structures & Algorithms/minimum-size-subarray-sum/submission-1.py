class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        k=[0]*(len(nums)+1)
        for i in range(len(nums)):
            k[i+1]=k[i]+nums[i]
        s=len(nums)+1
        for i in range(len(nums)):
            l,r=0,len(nums)
            while l<r:
                mid=(l+r)//2
                currSum=k[mid+1]-k[i]
                if currSum>=target:
                    r=mid
                else:
                    l=mid+1
            if l!=len(nums):
                s=min(l-i+1,s)
        return s%(len(nums)+1)