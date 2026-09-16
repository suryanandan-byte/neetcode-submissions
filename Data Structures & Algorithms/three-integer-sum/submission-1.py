class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            n,k=i+1,len(nums)-1
            while n<k:
                sum=nums[i]+nums[n]+nums[k]
                if sum>0:
                    k-=1
                elif sum<0:
                    n+=1
                else:
                    l.append([nums[i],nums[n],nums[k]])
                    n+=1
                    k-=1
                    while nums[n]==nums[n-1] and n<k:
                        n+=1
        return l