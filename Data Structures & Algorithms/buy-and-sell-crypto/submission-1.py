class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell=prices[-1]
        profit=0
        for i in range(len(prices)-1, -1, -1):
            profit=max(sell-prices[i], profit)
            sell=max(sell, prices[i])
        return profit