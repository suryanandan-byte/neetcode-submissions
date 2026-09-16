class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        n=len(a)
        l,h=0,n-1
        while(l<h):
            if a[h]+a[l]==target:
                break
            elif a[l]+a[h]>target:
                h-=1
            else:
                l+=1
        return [l+1,h+1]