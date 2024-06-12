class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice,maxProfit=99999,0
        for amt in prices:
            if amt < minPrice:
                minPrice=amt
            elif amt - minPrice > maxProfit:
                maxProfit = amt-minPrice
        return maxProfit