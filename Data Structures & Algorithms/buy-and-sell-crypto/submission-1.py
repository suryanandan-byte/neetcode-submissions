class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,n=0,1
        k=0
        while n<len(prices):
            if prices[l]<prices[n]:
                k=max(prices[n]-prices[l],k)
            else:
                l=n
            n+=1
        return k