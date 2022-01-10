class Solution:
    mem = {}

    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        if n not in self.mem:
            self.mem[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.mem[n]
