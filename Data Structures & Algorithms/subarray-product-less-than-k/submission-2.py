class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        prefix=[0]*(len(nums))
        c=1
        l=0
        for i in range(len(nums)):
            c*=nums[i]
            while c>=k:
                c//=nums[l]
                l+=1
            if i==0:
                prefix[i]=(i-l)+1
            else:
                prefix[i]=prefix[i-1]+(i-l+1)
        return prefix[-1]
            