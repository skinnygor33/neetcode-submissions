class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smaller = prices[0]
        for i in range(len(prices)):
            smaller = min(smaller,prices[i])
            profit = max(profit, prices[i] - smaller)
        return profit