class Solution:
    def maxProfit(self, prices):
        profit = 0
        # each day, if price increases sell over previous day's price, else don't sell, move on
        for i in range(1, len(prices)):
            profit += max(prices[i] - prices[i - 1], 0)
        return profit
