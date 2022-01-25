class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        size = len(nums)
        for i in range(size):
            if nums[i] <= 0:
                nums[i] = size+1
        for i in range(size):
            if 0 < abs(nums[i]) <= size:
                nums[abs(nums[i])-1] = -1 * abs(nums[abs(nums[i])-1])
        for i in range(size):
            if nums[i] > 0:
                return i+1
        return size+1
