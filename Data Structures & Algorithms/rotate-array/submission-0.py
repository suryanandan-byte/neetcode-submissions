class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        c=m=0
        while c<n:
            a=m
            prev=nums[m]
            while True:
                b=(a+k)%n
                nums[b],prev=prev,nums[b]
                c+=1
                a=b
                if m==a:
                    break
            m+=1