class Solution:
    def myAtoi(self, s):
        start = 0
        while start < len(s) and s[start] == " ":
            start += 1
        if start == len(s):
            return 0

        if s[start] == "-":
            sign = -1
            start += 1
        else:
            sign = 1
            if s[start] == "+":
                start += 1
        i = start
        while i < len(s):
            if not s[i].isnumeric():
                break
            i += 1

        output = 0 if start == i else sign * int(float(s[start:i]))
        if output > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif output < -1 * pow(2, 31):
            return -1 * pow(2, 31)
        else:
            return output
