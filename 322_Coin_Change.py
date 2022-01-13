class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        maxim = float('inf')
        dp = [0]
        for i in range(1, amount + 1):
            dp.append(min([1 + dp[i - x] if i - x >= 0 else maxim for x in coins]))
        return dp[amount] if dp[amount] < maxim else -1
