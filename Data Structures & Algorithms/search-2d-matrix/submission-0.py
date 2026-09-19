class Solution:
    def binary1(self,nums:List[List[int]],k:int,l:int,r:int)->int:
        if l<=r:
            mid=(l+r)//2
            if nums[mid][0]<=k and nums[mid][-1]>=k:
                return mid
            elif nums[mid][0]>k:
                return self.binary1(nums,k,l,mid-1)
            else:
                return self.binary1(nums,k,mid+1,r)
        return -1
    def binary2(self,nums:List[int],k:int,l:int,r:int)->bool:
        if l<=r:
            mid=(l+r)//2
            if nums[mid]==k:
                return True
            elif nums[mid]>k:
                return self.binary2(nums,k,l,mid-1)
            else:
                return self.binary2(nums,k,mid+1,r)
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c=self.binary1(matrix,target,0,len(matrix)-1)
        if c==-1:
            return False
        c=self.binary2(matrix[c],target,0,len(matrix[0])-1)
        return c