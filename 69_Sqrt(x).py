class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        y = 2
        while y * y < x:
            y *= 2
        minm = y / 2
        maxm = y

        while minm <= maxm:
            val = (minm + maxm) // 2
            if val * val <= x:
                if (val + 1) * (val + 1) > x:
                    return int(val)
                else:
                    minm = val + 1
            else:
                maxm = val - 1
        return int(val)
