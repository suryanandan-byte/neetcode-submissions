class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        for i in range(len(nums)):
            if target-nums[i] in l:
                return [l[target-nums[i]],i]
            l[nums[i]]=i
        
        