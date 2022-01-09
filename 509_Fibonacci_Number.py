class Solution:
    mem = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n not in self.mem:
            self.mem[n] = self.fib(n-1) + self.fib(n-2)
        return self.mem[n]
