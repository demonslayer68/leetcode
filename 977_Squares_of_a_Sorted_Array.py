class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        out = []
        j = 1
        if len(nums) == 1:
            return [nums[0] * nums[0]]
        while j < len(nums) and nums[j] < 0:
            j += 1
        i = j - 1
        while i >= 0 or j < len(nums):
            if i < 0 or (j < len(nums) and abs(nums[i]) > nums[j] ):
                out.append(nums[j] * nums[j])
                j += 1
            else:
                out.append(nums[i] * nums[i])
                i -= 1
        return out

obj = Solution()
obj.sortedSquares([-5,-3,-2,-1])