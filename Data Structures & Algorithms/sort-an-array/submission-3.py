import random
class Solution:
    def partition(self,nums:List[int],l:int ,h:int)->int:
        rand_idx = random.randint(l, h)
        nums[rand_idx], nums[h] = nums[h], nums[rand_idx]
        n=l-1
        for j in range(l,h):
            if nums[j]<=nums[h]:
                n+=1
                nums[n],nums[j]=nums[j],nums[n]
        nums[n+1],nums[h]=nums[h],nums[n+1]
        return n+1
            
    def quicksort(self,nums: List[int],l:int,h:int)->None:
        if l<h:
            k=self.partition(nums,l,h)
            self.quicksort(nums,l,k-1)
            self.quicksort(nums,k+1,h)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums,0,len(nums)-1)
        return nums