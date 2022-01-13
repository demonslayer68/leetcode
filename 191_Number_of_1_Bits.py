class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        binary = binary[2:]
        # This should be faster than collections.Counter
        return binary.count("1")
