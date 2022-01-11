class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob_Linear(arr):
            prev = 0
            prevprev = 0
            current = 0
            for num in arr:
                current = max(num + prevprev, prev)
                prevprev = prev
                prev = current
            return current
        return max(nums[0], rob_Linear(nums[1:]), rob_Linear(nums[:-1]))

obj = Solution()
print(obj.rob([1,2,3,1]))
