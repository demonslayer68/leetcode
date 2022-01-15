class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxprod = float("-inf")
        currentpos = 1
        currentneg = 1
        for i in range(len(nums)):
            newcurrentpos = max(currentneg * nums[i], currentpos * nums[i], nums[i])
            currentneg = min(currentneg * nums[i], currentpos * nums[i], nums[i])
            currentpos = newcurrentpos
            maxprod = max(maxprod, currentpos)
            print(currentpos, currentneg, maxprod)
        return maxprod

