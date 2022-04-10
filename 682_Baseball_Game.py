class Solution:
    def calPoints(self, ops: List[str]) -> int:
        i = 0
        while i < len(ops):
            if ops[i] == "C":
                del (ops[i])
                del (ops[i - 1])
                i -= 1
            elif ops[i] == "D":
                ops[i] = ops[i - 1] * 2
                i += 1
            elif ops[i] == "+":
                ops[i] = ops[i - 2] + ops[i - 1]
                i += 1
            else:
                ops[i] = int(ops[i])
                i += 1
        return sum(ops)
