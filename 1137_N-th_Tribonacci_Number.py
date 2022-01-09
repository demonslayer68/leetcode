class Solution:
    mem = {}
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif n not in self.mem:
            self.mem[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.mem[n]
