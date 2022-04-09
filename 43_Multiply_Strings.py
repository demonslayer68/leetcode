class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # multiply each digit of second number with first number.
        output = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                k = i + j + 1
                # print(i, j, k, output)
                carry = (output[k] + int(num1[i]) * int(num2[j])) // 10
                output[k] = (output[k] + int(num1[i]) * int(num2[j])) % 10
                while carry:
                    output[k - 1], carry = (carry + output[k - 1]) % 10, (carry + output[k - 1]) // 10
                    k -= 1

        while output[0] == 0 and len(output) > 1:
            del (output[0])

        str_output = ''.join(str(digit) for digit in output)
        return str_output
