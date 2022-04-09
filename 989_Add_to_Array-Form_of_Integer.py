class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        for i in range(len(num) - 1, -1, -1):
            if k == 0 and carry == 0:
                break
            carry, num[i] = ( num[i] + (k % 10 ) + carry ) // 10, ( num[i] + (k % 10 ) + carry ) % 10
            k = k // 10
        while k > 0 or carry > 0:
            num.insert(0, (k % 10 + carry) % 10 )
            carry = (k % 10 + carry) // 10
            k = k // 10
        return num