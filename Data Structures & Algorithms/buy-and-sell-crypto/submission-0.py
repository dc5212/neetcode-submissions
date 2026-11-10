class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<bp:
                bp=prices[i]
            profit=max(profit,prices[i]-bp)
        return profit