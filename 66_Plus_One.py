class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            carry = ( digits[i] + 1 ) // 10
            digits[i] = ( digits[i] + 1 ) % 10
            if not carry:
                break
        if carry and i == 0:
            digits.insert(0, 1)
        return digits