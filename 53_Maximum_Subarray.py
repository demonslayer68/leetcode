class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_contin = nums[0]
        output = nums[0]
        for i in range(1,len(nums)):
            max_contin = max(max_contin + nums[i], nums[i])
            output = max(output, max_contin)
        return output
