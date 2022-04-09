class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        output = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0 or carry > 0:
            # print(i, j, output)
            digit1 = 0 if i < 0 else int(num1[i])
            digit2 = 0 if j < 0 else int(num2[j])
            output = str((digit1 + digit2 + carry) % 10) + output
            carry = (digit1 + digit2 + carry) // 10
            i -= 1
            j -= 1
        return output if output else "0"
