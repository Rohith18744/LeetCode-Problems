class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal=prices[0]
        ans=0
        for i in range(len(prices)):
            ans=max(ans,(prices[i]-minVal)) 
            minVal=min(minVal,prices[i])
        return ans      