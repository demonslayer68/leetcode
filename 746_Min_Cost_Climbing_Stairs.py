class Solution:
    mem = {}

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        size = len(cost)

        def cost_recursive(n):
            if n == 0 or n == 1:
                return 0
            if n not in self.mem:
                self.mem[n] = min(cost[n-1] + cost_recursive(n - 1), cost[n-2] + cost_recursive(n - 2))
            return self.mem[n]
        return cost_recursive(size)
