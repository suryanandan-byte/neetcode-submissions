class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        x=0
        c=1
        l=0
        for i in range(len(nums)):
            c*=nums[i]
            while l<=i and c>=k:
                c//=nums[l]
                l+=1
            x+=(i-l+1)
        return x
            