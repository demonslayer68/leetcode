class Solution:
    def rob(self, nums: list[int]) -> int:
        prev = 0
        prevprev = 0
        current = 0
        for num in nums:
            current = max(num + prevprev, prev)
            prevprev = prev
            prev = current
        return current

obj = Solution()
print(obj.rob([1,2,3,1]))
