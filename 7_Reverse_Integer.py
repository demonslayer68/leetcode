class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = "-"
            x = -x
        elif x > 0:
            s = ""
        else:
            s = "0"
        while x:
            s = s + str(x % 10)
            x = int(x / 10)
        s = int(s)
        if s > pow(2, 31) - 1 or s < -pow(2, 31):
            return 0
        else:
            return s


obj = Solution()
print(obj.reverse(12345))
